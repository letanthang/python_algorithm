import matplotlib.pyplot as plt
import networkx as nx


parents = []
subPaths = [2, 5]


def dfs(index, parent_nodes):
    if index >= len(binary_tree):
        return

    parent_nodes.append(index)
    if binary_tree[index] == subPaths[len(subPaths) - 1]:
        if check_match(parent_nodes, subPaths):
            print(parent_nodes)

    # highlight the visited path
    if index != 0:
        parent = (index - 1) // 2
        update_edge(G, (parent, index))

    dfs(index * 2 + 1, parent_nodes)
    dfs(index * 2 + 2, parent_nodes)

    parent_nodes.pop()


def build_graph(index):
    if index >= len(binary_tree):
        return
    if index != 0:
        parent = (index - 1) // 2
        G.add_edge(parent, index)
    build_graph(index * 2 + 1)
    build_graph(index * 2 + 2)


def update_edge(G, edge):
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
    if index >= len(binary_tree):
        return

    position[index] = (x, y)

    prepare_pos(index * 2 + 1, x - delta, y - 1, delta / 2)
    prepare_pos(index * 2 + 2, x + delta, y - 1, delta / 2)


def check_match(nodes, sub_paths):
    if len(sub_paths) > len(nodes):
        return False

    for i in reversed(range(len(sub_paths))):
        if nodes[i] != sub_paths[i]:
            return False
    return True


binary_tree = [3, 7, 4, 9, 6, 11, 33, 6]

G = nx.DiGraph()
plt.ion()
fig, ax = plt.subplots()
position = {}
prepare_pos(0, 0.5, 0.98, 0.01)

build_graph(0)
update(G)

dfs(0, parents)

plt.ioff()
plt.show()
