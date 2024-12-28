import matplotlib.pyplot as plt
import networkx as nx


subPaths = [4, 11]


def dfs(index, parent_node_values):
    if index >= len(binary_tree):
        return

    # assign statement always create a new variable - can't use append
    parent_node_values = parent_node_values + [binary_tree[index]]
    print(parent_node_values)

    # highlight the visited path
    if index != 0:
        parent = (index - 1) // 2
        update_edge(G, (parent, index))

    # find the subPaths
    if binary_tree[index] == subPaths[len(subPaths) - 1]:
        if check_match(parent_node_values, subPaths):
            update_vertex(G, index)

    dfs(index * 2 + 1, parent_node_values)
    dfs(index * 2 + 2, parent_node_values)


def build_graph(index):
    if index >= len(binary_tree):
        return
    if index != 0:
        parent = (index - 1) // 2
        G.add_edge(parent, index)
    build_graph(index * 2 + 1)
    build_graph(index * 2 + 2)


def update_vertex(G, node):
    nx.draw_networkx_nodes(G, position, nodelist=[node], node_color="blue", ax=ax)
    plt.draw()
    plt.pause(1)


def update_edge(G, edge):
    nx.draw_networkx_edges(G, position, edgelist=[edge], edge_color="red", ax=ax)
    plt.draw()
    plt.pause(2)


def update(G):
    ax.clear()

    # draw edges
    nx.draw(G, position, with_labels=False, node_color="lightblue", ax=ax)

    # draw vertex label
    custom_labels = to_labels(binary_tree)
    nx.draw_networkx_labels(G, position, labels=custom_labels, font_color="black")
    plt.draw()
    plt.pause(1)


def prepare_pos(index, x, y, delta):
    if index >= len(binary_tree):
        return

    position[index] = (x, y)

    prepare_pos(index * 2 + 1, x - delta, y - 1, delta / 2)
    prepare_pos(index * 2 + 2, x + delta, y - 1, delta / 2)


def check_match(node_values, sub_paths):
    if len(sub_paths) > len(node_values):
        return False
    parents = node_values[::-1]
    path = sub_paths[::-1]

    for i in range(len(path)):
        if parents[i] != path[i]:
            return False
    return True


def to_labels(arr):
    return {i: arr[i] for i in range(len(arr))}


binary_tree = [3, 7, 4, 9, 6, 11, 33, 6]

G = nx.DiGraph()
plt.ion()
fig, ax = plt.subplots()
position = {}
prepare_pos(0, 0.5, 0.98, 0.01)

build_graph(0)
update(G)

dfs(0, [])

plt.ioff()
plt.show()
