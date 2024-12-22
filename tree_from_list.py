import matplotlib.pyplot as plt
import networkx as nx
from operator import attrgetter

def kruskal(n, edges):
    global path_edges

    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G)
    draw(G, pos)


def draw(G, pos):
    """Visualize the graph at a particular step, showing edge weights."""
    plt.figure(figsize=(8, 6))

    # Draw the main graph structure
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=700,
        font_weight="bold",
    )

    # Highlight path edges in red
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="black")

    plt.pause(1)
    plt.draw()


a = list(range(10))
print(a)

edges = [(0, 1, 4), (0, 2, 4), (1, 2, 2), (1, 3, 6), (2, 3, 8)]
kruskal(4, edges)

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