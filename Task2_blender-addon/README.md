# Task 2: Blender Addon - Cube Distribution and Mesh Merger

## Overview
Blender addon with two feature sets:
1. **Cube Distribution**: Create N cubes in an m×n grid with validation
2. **Mesh Merging**: Merge meshes that share common faces

## Installation

**Method 1: Quick Test (Recommended)**
1. Open Blender → Scripting workspace
2. Open `cube_mesh_addon.py` in text editor
3. Click **▶ Run Script**
4. Press **N** in 3D Viewport → Click **"Task"** tab

**Method 2: Permanent Install**
1. Edit → Preferences → Add-ons → Install
2. Select `cube_mesh_addon.py` → Enable checkbox
3. Press **N** in 3D Viewport → **"Task"** tab

## Usage

### Distribute Cubes
1. Set "Number of Cubes" (N < 20)
2. Click "Distribute Cubes"
3. Cubes appear in m×n grid (e.g., N=9 → 3×3 grid)

### Delete Cubes
1. Select cubes (click or box-select with B key)
2. Click "Delete Cubes"

### Compose Mesh
1. Select 2+ touching meshes (must share a face)
2. Click "Compose Mesh"
3. Meshes merge, common face removed

## Testing

**Run Tests:**
1. Load addon first (run `cube_mesh_addon.py`)
2. Open `test_script.py` in text editor
3. Click **▶ Run Script**
4. Check System Console (Window → Toggle System Console)

**Expected:** 7/7 tests passed (100%)

## Features Implemented

✅ **Feature Set 1:**
- UI panel with N input
- Validation: N > 20 shows error
- Distribute N cubes in m×n grid
- Cubes in "Distributed Cubes" collection
- Delete selected cubes

✅ **Feature Set 2:**
- Compose Mesh button
- Detects common faces
- Merges only if common face exists
- Removes common face when merging

## Technical Notes

**Grid Algorithm:** `m = ceil(sqrt(N))`, `n = ceil(N/m)`

**Face Detection:** Compares vertices in world coordinates with 0.001 tolerance

**Dependencies:** Blender 3.0+, bpy, math

## Troubleshooting

- **Panel missing?** Press N key in 3D Viewport
- **"Out of range" error?** Use N ≤ 20
- **"No objects selected"?** Select cubes first
- **"No common face"?** Ensure meshes touch perfectly

---
Created for FOSSEE Screening Task 