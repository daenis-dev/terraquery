#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

import laspy
import numpy as np
from scipy.spatial import cKDTree


CLASS_GROUPS = {
    "structures": [6],
    "vegetation": [3, 4, 5],
    "utility": [20],
    "encroachment": [],
}

COLORS_16BIT = {
    3: (0, 65535, 12000),
    4: (0, 65535, 12000),
    5: (0, 65535, 12000),
    6: (65535, 36000, 0),
    20: (0, 38000, 65535),
}

DEFAULT_ENCROACHMENT_DISTANCE_M = 2.5
STRUCTURE_CLUSTER_EPS_M = 3.0
VEGETATION_CLUSTER_EPS_M = 3.0
VISUAL_BUFFER_M = 2.0

def compute_height_above_ground(classifications, xyz):
    ground_mask = classifications == 2

    if np.count_nonzero(ground_mask) > 100:
        ground_xy = xyz[ground_mask][:, :2]
        ground_z = xyz[ground_mask][:, 2]

        tree = cKDTree(ground_xy)
        _, nearest_idx = tree.query(xyz[:, :2], k=1, workers=-1)

        return xyz[:, 2] - ground_z[nearest_idx]

    return xyz[:, 2] - np.percentile(xyz[:, 2], 5)

def connected_components_from_mask_fast_grid(xy, mask, cell_size):
    indices = np.flatnonzero(mask)

    if len(indices) == 0:
        return []

    ix = np.floor(xy[indices, 0] / cell_size).astype(np.int64)
    iy = np.floor(xy[indices, 1] / cell_size).astype(np.int64)

    cells = {}
    for point_index, cx, cy in zip(indices, ix, iy):
        key = (int(cx), int(cy))
        cells.setdefault(key, []).append(point_index)

    visited = set()
    components = []

    for start_key in cells.keys():
        if start_key in visited:
            continue

        stack = [start_key]
        component_points = []

        while stack:
            key = stack.pop()

            if key in visited:
                continue

            visited.add(key)
            component_points.extend(cells[key])

            x0, y0 = key

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    neighbor = (x0 + dx, y0 + dy)

                    if neighbor in cells and neighbor not in visited:
                        stack.append(neighbor)

        components.append(np.asarray(component_points, dtype=np.int64))

    return components

def compute_ranked_encroachment_masks(
    classifications,
    xyz,
    distance_meters=DEFAULT_ENCROACHMENT_DISTANCE_M,
    min_height_meters=None,
    min_cluster_size=None,
    ranking_type="point_count",
    top_n=None,
):
    structure_mask = classifications == 6
    veg_mask = np.isin(classifications, [3, 4, 5])

    structure_idx = np.where(structure_mask)[0]
    veg_idx = np.where(veg_mask)[0]

    final_structure_mask = np.zeros(len(classifications), dtype=bool)
    final_veg_mask = np.zeros(len(classifications), dtype=bool)

    if len(structure_idx) == 0 or len(veg_idx) == 0:
        return final_structure_mask, final_veg_mask

    structure_xyz = xyz[structure_idx]
    veg_xyz = xyz[veg_idx]

    structure_xy = structure_xyz[:, :2]
    veg_xy = veg_xyz[:, :2]

    structure_tree = cKDTree(structure_xy)

    distances, nearest_structure_local = structure_tree.query(
        veg_xy,
        k=1,
        distance_upper_bound=distance_meters
    )

    nearby_veg_local = np.where(np.isfinite(distances))[0]

    if len(nearby_veg_local) == 0:
        return final_structure_mask, final_veg_mask

    nearby_structure_local = nearest_structure_local[nearby_veg_local]
    nearby_structure_local = nearby_structure_local[
        nearby_structure_local < len(structure_idx)
    ]

    seed_structure_global = structure_idx[np.unique(nearby_structure_local)]
    seed_veg_global = veg_idx[nearby_veg_local]

    seed_mask = np.zeros(len(classifications), dtype=bool)
    seed_mask[seed_structure_global] = True
    seed_mask[seed_veg_global] = True

    candidate_mask = structure_mask | veg_mask

    print("Computing height above ground...", flush=True)

    height_above_ground = compute_height_above_ground(classifications, xyz)

    if min_height_meters is not None:
        candidate_mask &= height_above_ground >= min_height_meters

    candidate_xy = xyz[:, :2]

    print("Building clusters...", flush=True)

    raw_components = connected_components_from_mask_fast_grid(
        candidate_xy,
        seed_mask & candidate_mask,
        cell_size=max(STRUCTURE_CLUSTER_EPS_M, VEGETATION_CLUSTER_EPS_M)
    )

    print(f"Clusters found: {len(raw_components)}", flush=True)

    clusters = []

    for component_indices in raw_components:
        expanded_component_mask = np.zeros(len(classifications), dtype=bool)
        expanded_component_mask[component_indices] = True

        component_structure_mask = expanded_component_mask & structure_mask
        component_veg_mask = expanded_component_mask & veg_mask

        point_count = int(np.count_nonzero(component_structure_mask | component_veg_mask))

        if min_cluster_size is not None and point_count < min_cluster_size:
            continue

        component_mask = component_structure_mask | component_veg_mask
        max_height = float(np.max(height_above_ground[component_mask])) if point_count > 0 else 0.0

        if ranking_type == "height":
            score = max_height
        elif ranking_type == "severity":
            score = point_count * max(1.0, distance_meters)
        else:
            score = point_count

        clusters.append({
            "score": score,
            "point_count": point_count,
            "structure_indices": np.flatnonzero(component_structure_mask),
            "veg_indices": np.flatnonzero(component_veg_mask),
        })

    print(f"Rankable clusters after filters: {len(clusters)}", flush=True)
    clusters.sort(key=lambda cluster: cluster["score"], reverse=True)

    if top_n is not None:
        clusters = clusters[:top_n]

    for cluster in clusters:
        final_structure_mask[cluster["structure_indices"]] = True
        final_veg_mask[cluster["veg_indices"]] = True

    return final_structure_mask, final_veg_mask

def config_from_spec(spec):
    intent = spec.get("intent")
    target = spec.get("target")

    conditions = spec.get("conditions", {})
    proximity = conditions.get("proximity", {})
    proximity_object = proximity.get("object")
    distance_meters = proximity.get("distance_meters", DEFAULT_ENCROACHMENT_DISTANCE_M)

    filters = spec.get("filters", {}) or {}
    min_height_meters = filters.get("min_height_meters")
    min_cluster_size = filters.get("min_cluster_size")

    ranking = spec.get("ranking", {}) or {}
    ranking_type = ranking.get("type")
    top_n = ranking.get("top_n")

    render = spec.get("render", {}) or {}
    render_mode = render.get("mode")
    show = render.get("show", [])

    if intent != "encroachment_analysis":
        raise ValueError(f"Unsupported intent: {intent}")

    if target != "structures":
        raise ValueError(f"Unsupported target: {target}")

    if proximity_object != "vegetation":
        raise ValueError(f"Unsupported proximity object: {proximity_object}")

    if render_mode != "highlight":
        raise ValueError(f"Unsupported render.mode: {render_mode}")

    if not isinstance(show, list):
        raise ValueError("render.show must be a list")

    selected_groups = []

    for group in show:
        if group not in CLASS_GROUPS:
            raise ValueError(f"Unknown render.show group: {group}")

        if group not in selected_groups:
            selected_groups.append(group)

    if "encroachment" not in selected_groups:
        raise ValueError("encroachment_analysis requires render.show to include 'encroachment'")

    if top_n is not None:
        top_n = int(top_n)

    if min_cluster_size is not None:
        min_cluster_size = int(min_cluster_size)

    if min_height_meters is not None:
        min_height_meters = float(min_height_meters)

    if ranking_type is None:
        ranking_type = "point_count"

    if ranking_type not in ["point_count", "height", "severity"]:
        raise ValueError(f"Unsupported ranking.type: {ranking_type}")

    return {
        "selected_groups": selected_groups,
        "distance_meters": float(distance_meters),
        "min_height_meters": min_height_meters,
        "min_cluster_size": min_cluster_size,
        "ranking_type": ranking_type,
        "top_n": top_n,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--groups", required=False)
    parser.add_argument("--spec", required=False)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    distance_meters = DEFAULT_ENCROACHMENT_DISTANCE_M

    config = None

    if args.spec:
        spec = json.loads(args.spec)
        config = config_from_spec(spec)
        selected_groups = config["selected_groups"]
        distance_meters = config["distance_meters"]
    elif args.groups:
        selected_groups = [g.strip() for g in args.groups.split(",") if g.strip()]
        distance_meters = DEFAULT_ENCROACHMENT_DISTANCE_M
    else:
        raise ValueError("Either --groups or --spec is required")

    selected_classes = set()

    for group in selected_groups:
        if group not in CLASS_GROUPS:
            raise ValueError(f"Unknown group: {group}")

        selected_classes.update(CLASS_GROUPS[group])

    print("Reading LAS...", flush=True)

    las = laspy.read(str(input_path))

    # Convert to point format 7 so standard LAS RGB fields exist.
    out = laspy.convert(las, point_format_id=7)

    classifications = np.asarray(out.classification)
    intensity = np.asarray(out.intensity)

    # Flat neutral context is easier to read than raw intensity, which can create
    # scan-line artifacts / noisy striping in LiDAR tiles.
    context_gray = np.full(len(classifications), 43000, dtype=np.uint16)

    red = context_gray.copy()
    green = context_gray.copy()
    blue = context_gray.copy()

    # Basic class filters.
    restrict_to_analysis_mask = (
        config is not None
        and (
            config["top_n"] is not None
            or config["min_height_meters"] is not None
            or config["min_cluster_size"] is not None
        )
    )

    for class_id in selected_classes:
        if restrict_to_analysis_mask and class_id in {3, 4, 5, 6}:
            continue

        mask = classifications == class_id
        r, g, b = COLORS_16BIT[class_id]
        red[mask] = r
        green[mask] = g
        blue[mask] = b

    # Encroachment analysis.
    if "encroachment" in selected_groups:
        xyz = np.column_stack((out.x, out.y, out.z))

        if config is not None:
            encroachment_structure_mask, encroachment_veg_mask = compute_ranked_encroachment_masks(
                classifications,
                xyz,
                distance_meters=config["distance_meters"],
                min_height_meters=config["min_height_meters"],
                min_cluster_size=config["min_cluster_size"],
                ranking_type=config["ranking_type"],
                top_n=config["top_n"],
            )
        else:
            encroachment_structure_mask, encroachment_veg_mask = compute_ranked_encroachment_masks(
                classifications,
                xyz,
                distance_meters=distance_meters
            )

        # Encroaching vegetation = bright red.
        red[encroachment_veg_mask] = 65535
        green[encroachment_veg_mask] = 0
        blue[encroachment_veg_mask] = 0

        # Impacted structures = bright yellow/orange.
        red[encroachment_structure_mask] = 65535
        green[encroachment_structure_mask] = 42000
        blue[encroachment_structure_mask] = 0

    out.red = red
    out.green = green
    out.blue = blue

    out.write(str(output_path))


if __name__ == "__main__":
    main()