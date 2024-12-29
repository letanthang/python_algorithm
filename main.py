import networkx as nx
from dijsktra import dijkstra_visualized
from disjoint_set import DisjointSet
from kruskal import Edge, kruskal


def play_with_disjoint_set():
    ds = DisjointSet(5)
    ds.union(0, 2)
    ds.union(4, 2)
    ds.union(3, 1)

    print("Is 0 connected to 4:", ds.is_connected(0, 4))  # True
    print("Is 1 connected to 4:", ds.is_connected(1, 4))  # False

    ds.debug()
    ds.print_sets()


def play_with_kruskal():
    edges = [Edge(0, 1, 4), Edge(0, 2, 4), Edge(1, 2, 2), Edge(1, 3, 6), Edge(2, 3, 8)]
    # draw_graph_with_edges(edges)

    mst = kruskal(4, edges)
    for edge in mst:
        print(f"Edge: ({edge.u}, {edge.v}), Weight: {edge.weight}")


# def play_with_dijkstra():
# Create a weighted graph
# G = nx.Graph()
# edges = [(1, 2, 4), (1, 3, 1), (2, 3, 2), (2, 4, 5), (3, 4, 8)]
# G.add_weighted_edges_from(edges)
#
# # Find the shortest path
# dijkstra_visualized(G, 1, 4)


play_with_kruskal()
