# FOSSEE Screening Task Submission

**Candidate:** Kriti Gupta  
**Email:** kriti.gupta20004@gmail.com  

---

## Submission Contents

```
Kriti_Gupta.zip
├── README.md                    # main Documenation
├── Resume.pdf                   # Updated resume
├── SOP.pdf                      # Statement of Purpose
├── Task1_bintree-yaml/       # Binary Tree with YAML Integration
│   ├── bintree_yaml/            # Package source code
│   ├── tests/                   # Test suite
│   ├── main.py                  # Demo/test runner
│   ├── setup.py                 # Package installer
│   └── README.md                # Detailed documentation
└── Task2_blender-addon/      # Blender Addon
    ├── cube_mesh_addon.py       # Main addon file
    ├── test_script.py           # Test suite (7 tests)
    └── README.md                # Installation & usage guide
```

---

## Task 1: Binary Tree Implementation with YAML Integration

### Overview
A pip-installable Python package implementing binary tree data structures with YAML serialization/deserialization capabilities.

### Features Implemented
 **Core Features:**
- Binary tree with insert, search, delete operations
- Path-based node access (e.g., "L", "R", "LL", "LR")
- YAML import/export functionality
- Tree visualization and traversal methods

 **Bonus Features:**
- General tree (N-ary tree) support
- Tree statistics: height, balance factor, node counting
- Comprehensive error handling
- Edge case management

### Quick Start
```bash
cd Task1_bintree-yaml
pip install -e .
python main.py
```

### Testing
The package includes comprehensive tests covering:
- Core binary tree operations
- YAML import/export
- N-ary tree functionality
- Edge cases and error handling

**Expected Output:** All tests pass with detailed logs

**Full Documentation:** See `Task1_bintree-yaml/README.md`

---

## Task 2: Blender Addon - Cube Distribution & Mesh Merger

### Overview
A Blender addon providing intelligent cube distribution in grids and mesh merging with face detection.

### Features Implemented
 **Feature Set 1: Cube Distribution**
- UI panel with number input (N < 20 validation)
- Distributes N cubes in optimal m×n grid
- Cubes organized in separate collection
- Delete selected cubes functionality
- Automatic spacing to prevent overlaps

 **Feature Set 2: Mesh Merging**
- Compose Mesh button for merging
- Detects common faces between meshes
- Only merges when meshes share a face
- Removes internal faces at merge seam
- Proper error handling with user feedback

### Installation

**Method 1: Quick Test**
1. Open Blender → Scripting workspace
2. Open `cube_mesh_addon.py` in text editor
3. Click **▶ Run Script**
4. Press **N** → Click **"Task"** tab

**Method 2: Permanent Install**
1. Edit → Preferences → Add-ons → Install
2. Select `cube_mesh_addon.py` → Enable

### Testing
```
1. Load addon: Run cube_mesh_addon.py
2. Run tests: Open test_script.py → Run Script
3. Check console: 7/7 tests should pass
```

 **Full Documentation:** See `Task2_blender-addon/README.md`

---

## 💻 System Requirements

### Task 1: Binary Tree Package
- **Python:** 3.7 or higher
- **Dependencies:** PyYAML >= 5.1
- **OS:** Cross-platform (Windows, macOS, Linux)

### Task 2: Blender Addon
- **Blender:** 3.0 or higher (tested on 5.0.1)
- **Python:** Bundled with Blender (3.x)
- **OS:** Cross-platform

---

## Requirements Compliance

### Code Quality
-  Well-structured, modular code
-  Follows Python best practices (PEP 8)
-  Clear class and function names
-  Proper error handling

### Documentation
-  Comprehensive docstrings for all classes/methods
-  Inline comments explaining complex logic
-  README files with installation instructions
-  Usage examples and API documentation

### Testing
-  **Task 1:** Comprehensive test suite with multiple test cases
-  **Task 2:** 7 automated tests covering all features
-  Clear test output showing pass/fail status
-  Easy-to-run test scripts

### Bonus Features
-  **Task 1:** N-ary tree support + tree statistics
-  **Task 2:** All optional features implemented

---

## Quick Verification

### Task 1
```bash
cd Task1_bintree-yaml
pip install -e .
python main.py
# Expected: All tests pass
```

### Task 2
```
1. Open Blender
2. Load cube_mesh_addon.py
3. Run test_addon.py
# Expected: 7/7 tests passed (100%)
```

---

## 📝 Notes

- Both tasks are fully functional and tested
- All required and bonus features implemented
- Code follows professional software development practices
- Documentation is comprehensive and clear
- Test suites verify correctness of all features
