class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

def array_to_binary_tree(arr):
    def build_tree(index):
        # Base case: if index is out of bounds, return None
        if index >= len(arr) or arr[index] is None:
            return None
        
        # Create the current node
        node = TreeNode(arr[index])
        
        # Recursively build left and right children
        node.left = build_tree(2 * index + 1)
        node.right = build_tree(2 * index + 2)
        
        return node
    
    # Start building the tree from the root (index 0)
    return build_tree(0)

# Example usage:
array = [1, 2, 3, 4, 5, 6, 7]
root = array_to_binary_tree(array)

# Function to print the tree (in-order traversal)
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value, end=" ")
        in_order_traversal(node.right)

# Print the tree
in_order_traversal(root)