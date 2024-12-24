import matplotlib.pyplot as plt
import networkx as nx


def dfs(index):
    if index > len(binary_tree):
        return
    if index != 0:
        parent = (index - 1) // 2
        updateEdge(G, (parent, index))

    dfs(index * 2 + 1)
    dfs(index * 2 + 2)


def build_graph(index):
    if index > len(binary_tree):
        return
    if index != 0:
        parent = (index - 1) // 2
        G.add_edge(parent, index)
    build_graph(index * 2 + 1)
    build_graph(index * 2 + 2)


def updateEdge(G, edge):
    nx.draw_networkx_edges(G, position, edgelist=[edge], edge_color="red", ax=ax)
    plt.draw()
    plt.pause(1)


def update(G):
    ax.clear()

    nx.draw(
        G,
        position,
        with_labels=True,
        node_color="lightblue",
        ax=ax,
    )
    plt.draw()
    plt.pause(1)


def prepare_pos(index, x, y, delta):
    if index > len(binary_tree):
        return

    position[index] = (x, y)

    prepare_pos(index * 2 + 1, x - delta, y - 1, delta / 2)
    prepare_pos(index * 2 + 2, x + delta, y - 1, delta / 2)


binary_tree = [3, 7, 4, 9, 6, 11, 33, 6]

G = nx.DiGraph()
plt.ion()
fig, ax = plt.subplots()
position = {}
prepare_pos(0, 0.5, 0.98, 0.01)

build_graph(0)
update(G)

dfs(0)

plt.ioff()
plt.show()
