import matplotlib.pyplot as plt
import networkx as nx
from disjoint_set import DisjointSet

def visualize_step(G, pos, path_edges, current_node=None):
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

    # Highlight the current node in green
    if current_node is not None:
        nx.draw_networkx_nodes(
            G, pos, nodelist=[current_node], node_color="green", node_size=700
        )

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="black")

    plt.pause(1)
    plt.draw()


def dijkstra_visualized(G, start, target):
    pos = nx.spring_layout(G)  # Position layout for consistent visualization
    path_edges = []
    visited = set()
    distances = {node: float("inf") for node in G.nodes}
    distances[start] = 0

    while len(visited) < len(G.nodes):
        # Find the unvisited node with the smallest distance
        current_node = min(
            (node for node in G.nodes if node not in visited),
            key=lambda node: distances[node],
        )

        # Stop if the target node is reached
        if current_node == target:
            break

        # Visualize the step
        visualize_step(G, pos, path_edges, current_node)
        visited.add(current_node)

        # Update distances to neighbors
        for neighbor in G.neighbors(current_node):
            if neighbor not in visited:
                new_distance = (
                    distances[current_node] + G[current_node][neighbor]["weight"]
                )
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    path_edges.append((current_node, neighbor))

    # Final visualization of the shortest path
    visualize_step(G, pos, path_edges)


def demo():
    # Create a weighted graph
    G = nx.Graph()
    edges = [(1, 2, 4), (1, 3, 1), (2, 3, 2), (2, 4, 5), (3, 4, 8)]
    G.add_weighted_edges_from(edges)

    # Run Dijkstra's algorithm with visualization
    dijkstra_visualized(G, start=1, target=4)
