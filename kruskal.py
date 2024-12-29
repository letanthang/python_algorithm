from operator import attrgetter
from disjoint_set import DisjointSet
import matplotlib.pyplot as plt
import networkx as nx

path_edges = []


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


def kruskal(n, edges):
    global path_edges

    G = nx.Graph()
    es = edges_to_tuples(edges)
    G.add_weighted_edges_from(es)

    pos = nx.spring_layout(G)
    draw(G, pos)

    edges.sort(key=attrgetter("weight"))
    ds = DisjointSet(n)
    mst = []

    for edge in edges:
        if ds.find(edge.u) != ds.find(edge.v):
            mst.append(edge)
            path_edges.append((edge.u, edge.v, edge.weight))
            draw(G, pos)
            ds.union(edge.u, edge.v)
        if len(mst) == n - 1:
            break

    return mst


# Function to convert an object to a tuple
def to_tuple(edge: Edge):
    return edge.u, edge.v, edge.weight


def edges_to_tuples(edges):
    return list(map(to_tuple, edges))


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

    plt.pause(1.5)
    plt.draw()


edges = [Edge(0, 1, 4), Edge(0, 2, 4), Edge(1, 2, 2), Edge(1, 3, 6), Edge(2, 3, 8)]
# draw_graph_with_edges(edges)

mst = kruskal(4, edges)
for edge in mst:
    print(f"Edge: ({edge.u}, {edge.v}), Weight: {edge.weight}")

plt.show()
