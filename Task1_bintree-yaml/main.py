import yaml

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        pass
        
def print_tree(root, indent="", prefix="Root:", is_left=False):
    if root is None: 
        return
    
    print(f"{indent}{prefix}{root.value}")
    
    if root.left is not None or root.right is not None:
        if root.left is not None:
            print_tree(root.left, indent + "    ", "L---")
        if root.right is not None:
            print_tree(root.right, indent + "    ", "R---")

def add_node_by_path(root, path, value):
    if root is None or not path:
        return False
    
    current = root
    for direction in path[:-1]:
        if direction == 'L':
            if current.left is None:
                return False
            current = current.left
        elif direction == 'R':
            if current.right is None:
                return False
            current = current.right

    last_direction = path[-1]
    if last_direction == 'L':
        if current.left is not None:
            return False
        current.left = Node(value)
    elif last_direction == 'R':
        if current.right is not None:
            return False
        current.right = Node(value)

    return True

def edit_node(root, path, new_value):
    if root is None:
        return False
    
    if path == "":
        root.value = new_value
        return True
    
    current = root
    for direction in path:
        if direction == 'L':
            if current.left is None:
                return False
            current = current.left
        elif direction == 'R':
            if current.right is None:
                return False
            current = current.right
        else:
            return False
        
    current.value = new_value
    return True

def delete_node(root, path):
    if root is None or not path:
        return root
    
    if len(path) == 1:
        if path == "L":
            root.left = None
        elif path == "R":
            root.right = None
        return root
    
    current = root
    for direction in path[:-1]:
        if direction == 'L':
            if current.left is None:
                return root
            current = current.left
        elif direction == 'R':
            if current.right is None:
                return root
            current = current.right

    last_direction = path[-1]
    if last_direction == 'L':
        current.left = None
    elif last_direction == 'R':
        current.right = None

    return root

def delete_tree(root):
    if root is None:
        return None
    
    delete_tree(root.left)
    delete_tree(root.right)

    root.left = None
    root.right = None

    return None

def _build_tree_from_dict(data):
    if data is None or 'value' not in data:
        return None

    node = Node(data['value'])
    
    if 'left' in data and data['left'] is not None:
        node.left = _build_tree_from_dict(data['left'])
    
    if 'right' in data and data['right'] is not None:
        node.right = _build_tree_from_dict(data['right'])
    
    return node

def build_tree_from_yaml(filename):
    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
        
        return _build_tree_from_dict(data)
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None
    
def _tree_to_dict(node):
    if node is None:
        return None
    
    result = {'value': node.value}
    
    if node.left is not None:
        result['left'] = _tree_to_dict(node.left)
    
    if node.right is not None:
        result['right'] = _tree_to_dict(node.right)
    
    return result

def write_tree_to_yaml(root, filename):
    if root is None:
        print("Error: Cannot write empty tree")
        return False
    
    try:
        tree_dict = _tree_to_dict(root)
        
        with open(filename, 'w') as file:
            yaml.dump(tree_dict, file, default_flow_style=False, sort_keys=False)
        
        return True
    
    except Exception as e:
        print(f"Error writing YAML: {e}")
        return False
    
def print_tree_range(root, start_path="", depth=-1):
    if root is None:
        return
    
    current = root
    for direction in start_path:
        if direction == 'L':
            if current.left is None:
                return
            current = current.left
        elif direction == 'R':
            if current.right is None:
                return
            current = current.right
    
    # Print from this position with depth limit
    _print_tree_depth(current, "Root:", depth)


def _print_tree_depth(root, prefix, depth, indent=""):
    if root is None or depth == 0:
        return
    
    print(f"{indent}{prefix}{root.value}")
    
    # Calculate new depth
    new_depth = depth - 1 if depth > 0 else -1
    
    if root.left is not None or root.right is not None:
        if root.left is not None:
            _print_tree_depth(root.left, "L---", new_depth, indent + "    ")
        if root.right is not None:
            _print_tree_depth(root.right, "R---", new_depth, indent + "    ")

def create_tree(value):
    return Node(value)

#---------------------------------------------------------------------
# Bonus: General Tree (N-ary Tree)
# Allows nodes to have unlimited children instead of just left/right
#---------------------------------------------------------------------

class GeneralNode:
    """
    General Tree Node class - can have any number of children
    
    Attributes:
        value: The value stored in the node
        children: List of child nodes
    """
    
    def __init__(self, value):
        self.value = value
        self.children = []  
    
    def add_child(self, child):
        """Add a child node to this node"""
        self.children.append(child)

    
def create_general_tree(value):
    """
    Create a new general tree with a root node
        
    Args:
        value: The value for the root node
        
    Returns:
         GeneralNode: The root node
    """
    return GeneralNode(value)


def add_child_to_general_node(parent, value):
    """
    Add a child to a general tree node
    
    Args:
        parent: The parent GeneralNode
        value: Value for the new child
    
    Returns:
        GeneralNode: The newly created child node
    """
    child = GeneralNode(value)
    parent.add_child(child)
    return child

def print_general_tree(root, indent="", is_first=True):
    """
    Print a general tree structure
    
    Args:
        root: The root GeneralNode
        indent: Indentation string
        is_first: Whether this is the first call (root)
    """
    if root is None:
        return
    
    # Print current node
    if is_first:
        print(f"Root: {root.value}")
    else:
        print(f"{indent}Child: {root.value}")
    
    # Print all children with increased indentation
    for child in root.children:
        print_general_tree(child, indent + "    ", False)

def _build_general_tree_from_dict(data):
    """
    Helper to build general tree from dictionary
    
    Args:
        data: Dictionary containing node data
    
    Returns:
        GeneralNode: The constructed node
    """
    if data is None or 'value' not in data:
        return None
    
    node = GeneralNode(data['value'])
    
    # Check if there are children
    if 'children' in data and data['children'] is not None:
        for child_data in data['children']:
            child = _build_general_tree_from_dict(child_data)
            if child is not None:
                node.add_child(child)
    
    return node


def build_general_tree_from_yaml(filename):
    """
    Build a general tree from a YAML file
    
    Args:
        filename: Path to the YAML file
    
    Returns:
        GeneralNode: Root of the general tree
    """
    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
        
        if data is None:
            return None
        
        return _build_general_tree_from_dict(data)
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None
    
def _general_tree_to_dict(node):
    """
    Helper to convert general tree to dictionary
    
    Args:
        node: The GeneralNode to convert
    
    Returns:
        dict: Dictionary representation
    """
    if node is None:
        return None
    
    result = {'value': node.value}
    
    # Add children if they exist
    if node.children:
        result['children'] = [_general_tree_to_dict(child) for child in node.children]
    
    return result


def write_general_tree_to_yaml(root, filename):
    """
    Write a general tree to a YAML file
    
    Args:
        root: The root GeneralNode
        filename: Output filename
    
    Returns:
        bool: True if successful
    """
    if root is None:
        print("Error: Cannot write empty tree")
        return False
    
    try:
        tree_dict = _general_tree_to_dict(root)
        
        with open(filename, 'w') as file:
            yaml.dump(tree_dict, file, default_flow_style=False, sort_keys=False)
        
        return True
    
    except Exception as e:
        print(f"Error writing YAML: {e}")
        return False

#----------------------------------
# Extra Bonus Feature 1: Tree Statistics
#----------------------------------

def get_height(root):
    """
    Calculate the height of the tree
    Height = longest path from root to leaf
    
    Args:
        root: The root node of the tree
    
    Returns:
        int: Height of the tree (0 for single node, -1 for empty tree)
    """
    if root is None:
        return -1
    
    # Recursively get height of left and right subtrees
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    
    return max(left_height, right_height) + 1


def count_nodes(root):
    """
    Count total number of nodes in the tree
    
    Args:
        root: The root node of the tree
    
    Returns:
        int: Total number of nodes
    """
    if root is None:
        return 0
    
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_leaves(root):
    """
    Count the number of leaf nodes (nodes with no children)
    
    Args:
        root: The root node of the tree
    
    Returns:
        int: Number of leaf nodes
    """
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return 1
    
    return count_leaves(root.left) + count_leaves(root.right)


def is_balanced(root):
    """
    Check if the tree is balanced
    A balanced tree has left and right subtree heights differing by at most 1
    
    Args:
        root: The root node of the tree
    
    Returns:
        bool: True if balanced, False otherwise
    """
    if root is None:
        return True
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)

    if (abs(left_height - right_height) <=  1 and
        is_balanced(root.left) and 
        is_balanced(root.right)) :
        return True
    
    return False

#------------------------------------------
# Comprehensive tests for all features
#------------------------------------------

if __name__ == "__main__":
    print("--- Test 1: Basic Tree ---")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print_tree(root)
  
    print("\n--- Test 2: add_node_by_path ---")
    root2 = Node(10)
    print("Initial tree:")
    print_tree(root2)
    print("\nAdding nodes:")
    add_node_by_path(root2, "L", 5)
    add_node_by_path(root2, "R", 15)
    add_node_by_path(root2, "LL", 3)
    add_node_by_path(root2, "LR", 7)
    print("\nTree after additions:")
    print_tree(root2)
    
    print("\n--- Test 3: edit_node ---")
    print("Editing root to 100:")
    edit_node(root2, "", 100)
    print_tree(root2)
    print("\nEditing 'LL' to 30:")
    edit_node(root2, "LL", 30)
    print_tree(root2)
  
    print("\n--- Test 4: delete_node ---")
    print("Deleting 'LR':")
    root2 = delete_node(root2, "LR")
    print_tree(root2)

    print("\n--- Test 5: build_tree_from_yaml ---")
    yaml_file = "test.yaml"
    print(f"Building tree from '{yaml_file}':")
    yaml_tree = build_tree_from_yaml(yaml_file)
    if yaml_tree:
        print("Tree built from YAML:")
        print_tree(yaml_tree)

    print("\n--- Test 6: write_tree_to_yaml ---")
    output_file = "output.yaml"
    print(f"Writing tree to '{output_file}':")
    if write_tree_to_yaml(yaml_tree, output_file):
        print(f"Successfully wrote tree to '{output_file}'")
        print("\nReading it back:")
        verify_tree = build_tree_from_yaml(output_file)
        print_tree(verify_tree)

    print("\n--- Test 7: print_tree_range ---")
    print("Printing subtree from 'L' with depth 2:")
    print_tree_range(yaml_tree, "L", 2)

    print("\n--- BONUS Test: General Tree ---")
    # Create an organizational tree
    gen_root = create_general_tree("CEO")

    # Add children to CEO
    cto = add_child_to_general_node(gen_root, "CTO")
    cfo = add_child_to_general_node(gen_root, "CFO")
    coo = add_child_to_general_node(gen_root, "COO")

    # Add children to CTO
    add_child_to_general_node(cto, "Dev Manager 1")
    add_child_to_general_node(cto, "Dev Manager 2")
    add_child_to_general_node(cto, "QA Manager")

    # Add children to CFO
    add_child_to_general_node(cfo, "Accountant 1")
    add_child_to_general_node(cfo, "Accountant 2")

    # Add child to COO
    add_child_to_general_node(coo, "Operations Manager")

    print("General Tree Structure:")
    print_general_tree(gen_root)

    # Test YAML for general tree
    print("\n--- BONUS Test: General Tree YAML ---")
    gen_yaml_file = "general_tree.yaml"
    print(f"Writing general tree to '{gen_yaml_file}':")
    if write_general_tree_to_yaml(gen_root, gen_yaml_file):
        print(f"Successfully wrote to '{gen_yaml_file}'")

    # Read it back and verify
    print(f"\nReading general tree from '{gen_yaml_file}':")
    loaded_gen_tree = build_general_tree_from_yaml(gen_yaml_file)
    if loaded_gen_tree:
        print("Loaded General Tree:")
        print_general_tree(loaded_gen_tree)

    print("\n--- Extra BONUS Test 1: Tree Statistics ---")
    print(f"Height of tree: {get_height(root)}")
    print(f"Total nodes: {count_nodes(root)}")
    print(f"Leaf nodes: {count_leaves(root)}")
    print(f"Is balanced: {is_balanced(root)}")

    print(f"\nHeight of root2: {get_height(root2)}")
    print(f"Total nodes in root2: {count_nodes(root2)}")
    print(f"Is root2 balanced: {is_balanced(root2)}")

