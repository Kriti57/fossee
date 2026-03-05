# Binary Tree YAML Package

A Python package for binary tree operations with YAML integration.

## Overview

This package provides a complete implementation of binary trees with:
- Intuitive path-based node manipulation
- YAML serialization for data persistence
- Extended support for N-ary trees
- Statistical analysis tools

## Features

**Core:**
- Binary tree with path-based operations ("L", "R", "LL", etc.)
- Add, edit, delete nodes
- YAML import/export

**Bonus:**
- General tree (N-ary) with unlimited children
- Tree statistics (height, node count, balance check)

## Installation
```bash
pip install -e .
```

## Quick Start
```python
from main import *

# Binary Tree
root = Node(10)
add_node_by_path(root, "L", 5)
add_node_by_path(root, "R", 15)
print_tree(root)

# YAML
tree = build_tree_from_yaml("test.yaml")
write_tree_to_yaml(tree, "output.yaml")

# General Tree (Bonus)
gen_root = create_general_tree("CEO")
cto = add_child_to_general_node(gen_root, "CTO")
add_child_to_general_node(cto, "Dev Manager")
print_general_tree(gen_root)

# Statistics (Extra Bonus)
print(f"Height: {get_height(root)}")
print(f"Balanced: {is_balanced(root)}")
```

## Key Functions

**Binary Tree:**
- `add_node_by_path(root, path, value)` - Add node using path
- `edit_node(root, path, value)` - Edit node value
- `delete_node(root, path)` - Delete node
- `print_tree(root)` - Display tree

**YAML:**
- `build_tree_from_yaml(filename)` - Load from YAML
- `write_tree_to_yaml(root, filename)` - Save to YAML

**General Tree (Bonus):**
- `create_general_tree(value)` - Create N-ary tree
- `add_child_to_general_node(parent, value)` - Add child
- `print_general_tree(root)` - Display tree

**Statistics (Extra Bonus):**
- `get_height(root)` - Tree height
- `count_nodes(root)` - Total nodes
- `is_balanced(root)` - Balance check

## Path Notation

- "L" = left, "R" = right
- "LL" = left-left, "LR" = left-right, etc.

## Requirements

- Python >= 3.7
- PyYAML >= 5.1

---
Created for FOSSEE Screening Task