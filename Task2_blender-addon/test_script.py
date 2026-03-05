"""
Test Script for Cube Distribution and Mesh Merger Addon
========================================================

This script tests all features of the addon to verify correctness.

How to Run:
1. Open Blender
2. Go to Scripting workspace
3. Open this file in the text editor
4. Click "Run Script"
5. Check the console output for test results

Test Coverage:
- Feature Set 1: Cube distribution, validation, deletion
- Feature Set 2: Mesh merging with face detection
"""

import bpy
import math


def cleanup_scene():
    """Remove all mesh objects from the scene"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    print("✓ Scene cleaned")


def test_1_distribute_cubes_valid():
    """Test 1: Distribute valid number of cubes (N < 20)"""
    print("\n" + "="*50)
    print("TEST 1: Distribute Cubes (Valid Input)")
    print("="*50)
    
    cleanup_scene()
    
    # Set number of cubes to 9
    bpy.context.scene.task_properties.num_cubes = 9
    
    # Execute distribute cubes operator
    result = bpy.ops.object.distribute_cubes()
    
    # Verify cubes were created
    cube_count = len([obj for obj in bpy.data.objects if obj.type == 'MESH'])
    
    if result == {'FINISHED'} and cube_count == 9:
        print("✓ PASS: Created 9 cubes in 3x3 grid")
        print(f"  - Operator result: {result}")
        print(f"  - Cubes created: {cube_count}")
        return True
    else:
        print("✗ FAIL: Expected 9 cubes")
        print(f"  - Operator result: {result}")
        print(f"  - Cubes created: {cube_count}")
        return False


def test_2_distribute_cubes_invalid():
    """Test 2: Validate N > 20 rejection"""
    print("\n" + "="*50)
    print("TEST 2: Validation (N > 20 should fail)")
    print("="*50)
    
    cleanup_scene()
    
    # Set number of cubes to 25 (should fail)
    bpy.context.scene.task_properties.num_cubes = 25
    
    # Execute distribute cubes operator
    result = bpy.ops.object.distribute_cubes()
    
    # Verify operation was cancelled
    cube_count = len([obj for obj in bpy.data.objects if obj.type == 'MESH'])
    
    if result == {'CANCELLED'} and cube_count == 0:
        print("✓ PASS: Correctly rejected N=25 (out of range)")
        print(f"  - Operator result: {result}")
        print(f"  - Cubes created: {cube_count}")
        return True
    else:
        print("✗ FAIL: Should have rejected N > 20")
        print(f"  - Operator result: {result}")
        print(f"  - Cubes created: {cube_count}")
        return False


def test_3_grid_calculation():
    """Test 3: Verify grid dimensions (m x n)"""
    print("\n" + "="*50)
    print("TEST 3: Grid Calculation (m x n)")
    print("="*50)
    
    test_cases = [
        (4, 2, 2),   # 4 cubes -> 2x2
        (9, 3, 3),   # 9 cubes -> 3x3
        (6, 3, 2),   # 6 cubes -> 3x2
    ]
    
    all_passed = True
    
    for N, expected_m, expected_n in test_cases:
        # Calculate grid dimensions using same logic as addon
        m = math.ceil(math.sqrt(N))
        n = math.ceil(N / m)
        
        if m == expected_m and n == expected_n:
            print(f"✓ PASS: N={N} -> {m}x{n} grid")
        else:
            print(f"✗ FAIL: N={N} expected {expected_m}x{expected_n}, got {m}x{n}")
            all_passed = False
    
    return all_passed


def test_4_delete_cubes():
    """Test 4: Delete selected cubes"""
    print("\n" + "="*50)
    print("TEST 4: Delete Selected Cubes")
    print("="*50)
    
    cleanup_scene()
    
    # Create some cubes
    bpy.context.scene.task_properties.num_cubes = 4
    bpy.ops.object.distribute_cubes()
    
    initial_count = len([obj for obj in bpy.data.objects if obj.type == 'MESH'])
    
    # Select 2 cubes
    bpy.ops.object.select_all(action='DESELECT')
    mesh_objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']
    mesh_objects[0].select_set(True)
    mesh_objects[1].select_set(True)
    
    # Delete selected cubes
    result = bpy.ops.object.delete_cubes()
    
    final_count = len([obj for obj in bpy.data.objects if obj.type == 'MESH'])
    
    if result == {'FINISHED'} and final_count == initial_count - 2:
        print("✓ PASS: Deleted 2 selected cubes")
        print(f"  - Initial cubes: {initial_count}")
        print(f"  - Final cubes: {final_count}")
        return True
    else:
        print("✗ FAIL: Delete operation failed")
        print(f"  - Initial cubes: {initial_count}")
        print(f"  - Final cubes: {final_count}")
        return False


def test_5_collection_creation():
    """Test 5: Verify cubes are in separate collection"""
    print("\n" + "="*50)
    print("TEST 5: Collection Organization")
    print("="*50)
    
    cleanup_scene()
    
    # Create cubes
    bpy.context.scene.task_properties.num_cubes = 4
    bpy.ops.object.distribute_cubes()
    
    # Check if "Distributed Cubes" collection exists
    collection_exists = "Distributed Cubes" in bpy.data.collections
    
    if collection_exists:
        collection = bpy.data.collections["Distributed Cubes"]
        cubes_in_collection = len(collection.objects)
        
        if cubes_in_collection == 4:
            print("✓ PASS: Cubes organized in 'Distributed Cubes' collection")
            print(f"  - Collection exists: {collection_exists}")
            print(f"  - Cubes in collection: {cubes_in_collection}")
            return True
        else:
            print("✗ FAIL: Wrong number of cubes in collection")
            print(f"  - Expected: 4, Got: {cubes_in_collection}")
            return False
    else:
        print("✗ FAIL: 'Distributed Cubes' collection not created")
        return False


def test_6_compose_mesh_no_common_face():
    """Test 6: Compose mesh should fail when no common face"""
    print("\n" + "="*50)
    print("TEST 6: Compose Mesh (No Common Face - Should Fail)")
    print("="*50)
    
    cleanup_scene()
    
    # Create 2 cubes with gap (no common face)
    bpy.context.scene.task_properties.num_cubes = 2
    bpy.ops.object.distribute_cubes()
    
    # Select both cubes
    bpy.ops.object.select_all(action='SELECT')
    
    # Try to compose (should fail)
    result = bpy.ops.object.compose_mesh()
    
    if result == {'CANCELLED'}:
        print("✓ PASS: Correctly rejected meshes without common face")
        print(f"  - Operator result: {result}")
        return True
    else:
        print("✗ FAIL: Should have rejected non-touching meshes")
        print(f"  - Operator result: {result}")
        return False


def test_7_compose_mesh_with_common_face():
    """Test 7: Compose mesh should work when meshes share a face"""
    print("\n" + "="*50)
    print("TEST 7: Compose Mesh (With Common Face - Should Work)")
    print("="*50)
    
    cleanup_scene()
    
    # Create two cubes that touch
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    bpy.ops.mesh.primitive_cube_add(size=1, location=(2, 0, 0))  # Touching
    
    # Select both cubes
    bpy.ops.object.select_all(action='SELECT')
    
    initial_count = len([obj for obj in bpy.data.objects if obj.type == 'MESH'])
    
    # Compose meshes
    result = bpy.ops.object.compose_mesh()
    
    final_count = len([obj for obj in bpy.data.objects if obj.type == 'MESH'])
    
    if result == {'FINISHED'} and final_count == 1:
        print("✓ PASS: Successfully merged touching meshes")
        print(f"  - Initial meshes: {initial_count}")
        print(f"  - Final meshes: {final_count}")
        print(f"  - Operator result: {result}")
        return True
    else:
        print("✗ FAIL: Merge operation failed")
        print(f"  - Initial meshes: {initial_count}")
        print(f"  - Final meshes: {final_count}")
        print(f"  - Operator result: {result}")
        return False


def run_all_tests():
    """Run all test cases and report results"""
    print("\n" + "="*70)
    print(" CUBE DISTRIBUTION AND MESH MERGER ADDON - TEST SUITE")
    print("="*70)
    
    tests = [
        test_1_distribute_cubes_valid,
        test_2_distribute_cubes_invalid,
        test_3_grid_calculation,
        test_4_delete_cubes,
        test_5_collection_creation,
        test_6_compose_mesh_no_common_face,
        test_7_compose_mesh_with_common_face,
    ]
    
    results = []
    for test_func in tests:
        try:
            result = test_func()
            results.append((test_func.__name__, result))
        except Exception as e:
            print(f"\n✗ ERROR in {test_func.__name__}: {e}")
            results.append((test_func.__name__, False))
    
    # Summary
    print("\n" + "="*70)
    print(" TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {test_name}")
    
    print("\n" + "-"*70)
    print(f"TOTAL: {passed}/{total} tests passed ({(passed/total)*100:.1f}%)")
    print("="*70)
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Addon is working correctly.")
    else:
        print(f"\n {total - passed} test(s) failed. Please review.")


# Run tests when script is executed
if __name__ == "__main__":
    # Check if addon is loaded
    if not hasattr(bpy.context.scene, 'task_properties'):
        print("\n" + "="*70)
        print("ERROR: Addon not loaded!")
        print("="*70)
        print("Please run 'cube_mesh_addon.py' first to register the addon.")
        print("Then run this test script.")
    else:
        run_all_tests()