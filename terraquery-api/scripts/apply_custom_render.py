#!/usr/bin/env python3
import argparse
from pathlib import Path

import laspy
import numpy as np
from scipy.spatial import cKDTree


GROUND_CLASS = 2
CUSTOM_VEGETATION_CLASS = 3
CUSTOM_STRUCTURE_CLASS = 6
CUSTOM_OTHER_CLASS = 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    source_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    las = laspy.read(str(source_path))

    x = np.asarray(las.x)
    y = np.asarray(las.y)
    z = np.asarray(las.z)
    original_class = np.asarray(las.classification)

    ground_mask = original_class == GROUND_CLASS

    if np.count_nonzero(ground_mask) > 100:
        ground_xy = np.column_stack((x[ground_mask], y[ground_mask]))
        ground_z = z[ground_mask]

        tree = cKDTree(ground_xy)
        _, nearest_idx = tree.query(np.column_stack((x, y)), k=1, workers=-1)
        height_above_ground = z - ground_z[nearest_idx]
    else:
        height_above_ground = z - np.percentile(z, 5)

    # KyFromAbove tile dimensions are in feet-like projected units.
    # Use conservative thresholds:
    # - above-ground object candidate: > 6 ft
    # - likely structure: flatter elevated surfaces
    # - likely vegetation: elevated rough/non-flat surfaces
    xy_cell_size = 10.0
    min_object_height = 6.0
    max_structure_height = 80.0
    max_structure_roughness = 5.0
    min_structure_cell_points = 8

    ix = np.floor(x / xy_cell_size).astype(np.int64)
    iy = np.floor(y / xy_cell_size).astype(np.int64)

    cell_key = ix.astype(np.int64) * 10_000_000 + iy.astype(np.int64)

    order = np.argsort(cell_key)
    sorted_keys = cell_key[order]
    sorted_z = z[order]

    unique_keys, starts, counts = np.unique(
        sorted_keys,
        return_index=True,
        return_counts=True,
    )

    cell_std_by_key = {}
    cell_count_by_key = {}

    for key, start, count in zip(unique_keys, starts, counts):
        cell_count_by_key[int(key)] = int(count)

        if count < 5:
            cell_std_by_key[int(key)] = 999.0
        else:
            cell_std_by_key[int(key)] = float(np.std(sorted_z[start:start + count]))

    roughness = np.array(
        [cell_std_by_key.get(int(k), 999.0) for k in cell_key],
        dtype=np.float32,
    )

    elevated = height_above_ground >= min_object_height

    existing_structure = original_class == 6
    existing_vegetation = np.isin(original_class, [3, 4, 5])

    cell_count = np.array(
        [cell_count_by_key.get(int(k), 0) for k in cell_key],
        dtype=np.int32,
    )

    inferred_structure_seed = (
        elevated
        & (height_above_ground <= max_structure_height)
        & (roughness <= max_structure_roughness)
        & (cell_count >= min_structure_cell_points)
    )

    # Expand structure labels to nearby elevated points, then clean up by object/component.
    # This helps fill whole roof surfaces while preventing mostly-vegetation clusters from becoming structure.
    inferred_vegetation_seed = elevated & ~inferred_structure_seed
    structure_seed_count = int(np.count_nonzero(inferred_structure_seed))

    if structure_seed_count > 0:
        structure_xy = np.column_stack((x[inferred_structure_seed], y[inferred_structure_seed]))
        candidate_mask = elevated & (height_above_ground <= max_structure_height)
        candidate_xy = np.column_stack((x[candidate_mask], y[candidate_mask]))

        structure_tree = cKDTree(structure_xy)
        distances, _ = structure_tree.query(
            candidate_xy,
            k=1,
            distance_upper_bound=12.0,
            workers=-1,
        )

        candidate_indices = np.flatnonzero(candidate_mask)

        expanded_structure = inferred_structure_seed.copy()
        expanded_structure[candidate_indices[np.isfinite(distances)]] = True

        # Component cleanup in XY space.
        # Each connected mass is treated as one object.
        voxel_size = 6.0

        vx = np.floor(x / voxel_size).astype(np.int32)
        vy = np.floor(y / voxel_size).astype(np.int32)

        object_mask = elevated & (height_above_ground <= max_structure_height)

        grid = {}
        for i in np.flatnonzero(object_mask):
            key = (int(vx[i]), int(vy[i]))

            if key not in grid:
                grid[key] = []

            grid[key].append(i)

        grid_keys = list(grid.keys())
        key_to_idx = {key: idx for idx, key in enumerate(grid_keys)}

        adjacency = [[] for _ in range(len(grid_keys))]

        for idx, (gx, gy) in enumerate(grid_keys):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    neighbor = (gx + dx, gy + dy)
                    neighbor_idx = key_to_idx.get(neighbor)

                    if neighbor_idx is not None:
                        adjacency[idx].append(neighbor_idx)

        visited = set()
        components = []

        for idx in range(len(grid_keys)):
            if idx in visited:
                continue

            stack = [idx]
            component_grid_indices = []

            while stack:
                current = stack.pop()

                if current in visited:
                    continue

                visited.add(current)
                component_grid_indices.append(current)

                for neighbor in adjacency[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            components.append(component_grid_indices)

        component_vegetation_ratio_threshold = 0.55
        component_structure_seed_ratio_threshold = 0.14
        component_expanded_structure_ratio_threshold = 0.55
        min_component_points = 120

        final_structure = np.zeros_like(inferred_structure_seed)

        for component in components:
            point_indices = []

            for grid_idx in component:
                point_indices.extend(grid[grid_keys[grid_idx]])

            if len(point_indices) < min_component_points:
                continue

            point_indices = np.asarray(point_indices, dtype=np.int64)

            component_structure_seed_count = int(np.count_nonzero(inferred_structure_seed[point_indices]))
            component_expanded_structure_count = int(np.count_nonzero(expanded_structure[point_indices]))
            component_vegetation_seed_count = int(np.count_nonzero(inferred_vegetation_seed[point_indices]))

            structure_seed_ratio = component_structure_seed_count / len(point_indices)
            expanded_structure_ratio = component_expanded_structure_count / len(point_indices)
            vegetation_seed_ratio = component_vegetation_seed_count / len(point_indices)

            # If the mass is overwhelmingly vegetation, do not let a few flat/noisy points turn it into structure.
            if vegetation_seed_ratio >= component_vegetation_ratio_threshold:
                continue

            # If the component has enough structure signal, classify the whole connected object as structure.
            if (
                structure_seed_ratio >= component_structure_seed_ratio_threshold
                and expanded_structure_ratio >= component_expanded_structure_ratio_threshold
            ):
                final_structure[point_indices] = True

        inferred_structure = final_structure
    else:
        inferred_structure = inferred_structure_seed

    # Recompute vegetation AFTER final structure cleanup.
    # Anything elevated that is not final structure becomes vegetation.
    inferred_vegetation = elevated & ~inferred_structure

    custom_class = np.full(len(original_class), CUSTOM_OTHER_CLASS, dtype=np.uint8)
    custom_class[ground_mask] = GROUND_CLASS
    custom_class[existing_vegetation | inferred_vegetation] = CUSTOM_VEGETATION_CLASS
    custom_class[existing_structure | inferred_structure] = CUSTOM_STRUCTURE_CLASS

    out_header = laspy.LasHeader(
        point_format=las.header.point_format,
        version=las.header.version,
    )

    out_header.scales = las.header.scales
    out_header.offsets = las.header.offsets
    out_header.mins = las.header.mins
    out_header.maxs = las.header.maxs

    out_las = laspy.LasData(out_header)
    out_las.points = las.points.copy()
    out_las.classification = custom_class
    out_las.update_header()
    out_las.write(str(output_path))

    print("Custom classification complete")
    print("Ground:", int(np.count_nonzero(custom_class == GROUND_CLASS)))
    print("Vegetation:", int(np.count_nonzero(custom_class == CUSTOM_VEGETATION_CLASS)))
    print("Structures:", int(np.count_nonzero(custom_class == CUSTOM_STRUCTURE_CLASS)))
    print("Other:", int(np.count_nonzero(custom_class == CUSTOM_OTHER_CLASS)))


if __name__ == "__main__":
    main()