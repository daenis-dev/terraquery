#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

import laspy
import numpy as np
from scipy.spatial import cKDTree
from scipy import ndimage


GROUND_CLASS = 2
VEGETATION_CLASS = 3
STRUCTURE_CLASS = 6
OTHER_CLASS = 1


def height_above_nearest_ground(x, y, z, ground_mask):
    if np.count_nonzero(ground_mask) > 100:
        ground_xy = np.column_stack((x[ground_mask], y[ground_mask]))
        ground_z = z[ground_mask]
        tree = cKDTree(ground_xy)
        _, idx = tree.query(np.column_stack((x, y)), k=1, workers=-1)
        return z - ground_z[idx]

    return z - np.percentile(z, 5)


def grid_features(x, y, z, cell_size):
    ix = np.floor((x - x.min()) / cell_size).astype(np.int64)
    iy = np.floor((y - y.min()) / cell_size).astype(np.int64)
    key = ix * 10_000_000 + iy

    order = np.argsort(key)
    sorted_key = key[order]
    sorted_z = z[order]

    unique_keys, starts, counts = np.unique(
        sorted_key,
        return_index=True,
        return_counts=True,
    )

    z_std = {}
    z_range = {}
    point_count = {}

    for k, start, count in zip(unique_keys, starts, counts):
        vals = sorted_z[start:start + count]
        point_count[int(k)] = int(count)

        if count < 5:
            z_std[int(k)] = 999.0
            z_range[int(k)] = 999.0
        else:
            z_std[int(k)] = float(np.std(vals))
            z_range[int(k)] = float(np.max(vals) - np.min(vals))

    roughness = np.array([z_std.get(int(k), 999.0) for k in key], dtype=np.float32)
    vertical_range = np.array([z_range.get(int(k), 999.0) for k in key], dtype=np.float32)
    density = np.array([point_count.get(int(k), 0) for k in key], dtype=np.int32)

    return ix, iy, key, roughness, vertical_range, density


def connected_component_structure_fill(
    x,
    y,
    elevated,
    plausible_object,
    structure_seed,
    vegetation_seed,
    height_above_ground,
):
    voxel_size = 5.0

    gx = np.floor((x - x.min()) / voxel_size).astype(np.int32)
    gy = np.floor((y - y.min()) / voxel_size).astype(np.int32)

    width = int(gx.max()) + 1
    height = int(gy.max()) + 1

    object_grid = np.zeros((height, width), dtype=bool)
    seed_grid = np.zeros((height, width), dtype=bool)
    veg_grid = np.zeros((height, width), dtype=bool)

    object_grid[gy[plausible_object], gx[plausible_object]] = True
    seed_grid[gy[structure_seed], gx[structure_seed]] = True
    veg_grid[gy[vegetation_seed], gx[vegetation_seed]] = True

    object_grid = ndimage.binary_closing(
        object_grid,
        structure=np.ones((3, 3), dtype=bool),
        iterations=2,
    )

    labels, _ = ndimage.label(
        object_grid,
        structure=np.ones((3, 3), dtype=bool),
    )

    point_component = labels[gy, gx]

    component_ids = np.unique(point_component[plausible_object])
    component_ids = component_ids[component_ids != 0]

    final_structure = np.zeros_like(elevated, dtype=bool)

    min_component_points = 120
    min_structure_seed_ratio = 0.10
    max_vegetation_seed_ratio = 0.65

    for component_id in component_ids:
        component_mask = plausible_object & (point_component == component_id)
        component_count = int(np.count_nonzero(component_mask))

        if component_count < min_component_points:
            continue

        structure_seed_count = int(np.count_nonzero(structure_seed & component_mask))
        vegetation_seed_count = int(np.count_nonzero(vegetation_seed & component_mask))

        structure_seed_ratio = structure_seed_count / component_count
        vegetation_seed_ratio = vegetation_seed_count / component_count

        component_heights = height_above_ground[component_mask]
        height_spread = float(np.percentile(component_heights, 95) - np.percentile(component_heights, 5))

        # Buildings usually have enough planar/flat seed area.
        # Trees usually have high vegetation ratio and larger vertical spread.
        if vegetation_seed_ratio >= max_vegetation_seed_ratio and structure_seed_ratio < 0.20:
            continue

        if structure_seed_ratio >= min_structure_seed_ratio and height_spread <= 45.0:
            final_structure[component_mask] = True

    return final_structure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--manifest", required=False)
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
    existing_structure = original_class == STRUCTURE_CLASS
    existing_vegetation = np.isin(original_class, [3, 4, 5])

    height_above_ground = height_above_nearest_ground(x, y, z, ground_mask)

    # State-plane KyFromAbove units are effectively feet.
    min_object_height = 6.0
    max_structure_height = 90.0

    elevated = height_above_ground >= min_object_height
    plausible_object = elevated & (height_above_ground <= max_structure_height)

    _, _, _, roughness_8, vertical_range_8, density_8 = grid_features(x, y, z, 8.0)
    _, _, _, roughness_16, vertical_range_16, density_16 = grid_features(x, y, z, 16.0)

    # Structure seed:
    # flat-ish, dense, elevated surfaces.
    structure_seed = (
        plausible_object
        & (roughness_8 <= 4.5)
        & (vertical_range_8 <= 14.0)
        & (density_8 >= 8)
        & (roughness_16 <= 7.5)
    )

    # Vegetation seed:
    # elevated, rough/vertically variable, canopy-like.
    vegetation_seed = (
        elevated
        & (
            (roughness_8 > 4.5)
            | (vertical_range_8 > 14.0)
            | (vertical_range_16 > 22.0)
        )
    )

    # Preserve reliable existing labels if present.
    structure_seed = structure_seed | existing_structure
    vegetation_seed = vegetation_seed | existing_vegetation

    inferred_structure = connected_component_structure_fill(
        x=x,
        y=y,
        elevated=elevated,
        plausible_object=plausible_object,
        structure_seed=structure_seed,
        vegetation_seed=vegetation_seed,
        height_above_ground=height_above_ground,
    )

    inferred_vegetation = elevated & ~inferred_structure

    custom_class = np.full(len(original_class), OTHER_CLASS, dtype=np.uint8)
    custom_class[ground_mask] = GROUND_CLASS
    custom_class[inferred_vegetation] = VEGETATION_CLASS
    custom_class[inferred_structure] = STRUCTURE_CLASS

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

    manifest = {
        "status": "ok",
        "source": str(source_path),
        "output": str(output_path),
        "classes": {
            "ground": int(np.count_nonzero(custom_class == GROUND_CLASS)),
            "vegetation": int(np.count_nonzero(custom_class == VEGETATION_CLASS)),
            "structures": int(np.count_nonzero(custom_class == STRUCTURE_CLASS)),
            "other": int(np.count_nonzero(custom_class == OTHER_CLASS)),
        },
        "method": "height-normalized object-based classification using ground normalization, local roughness, vertical range, density, and connected-component cleanup",
    }

    if args.manifest:
        manifest_path = Path(args.manifest)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(manifest, indent=2))

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()