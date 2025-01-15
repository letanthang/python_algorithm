import matplotlib.pyplot as plt
import networkx as nx
from operator import attrgetter
path_edges = []

def drawEdges(edges):
    global path_edges

    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G)
    updateGraph(G, pos)   

def drawEdgesByOne(edges):
    global path_edges

    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    pos = nx.spring_layout(G)
    updateGraph(G, pos)        


def updateGraph(G, pos):
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
drawEdges(edges)