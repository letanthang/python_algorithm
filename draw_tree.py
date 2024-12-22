import matplotlib.pyplot as plt
import networkx as nx


def dfs(index):
    if index > len(binary_tree):
        return
    if index != 0:
        parent = (index - 1) // 2
        G.add_edge(parent, index)
        update(G)

    dfs(index * 2 + 1)
    dfs(index * 2 + 2)


def update(G):
    ax.clear()

    nx.draw(G, position, with_labels=True, node_color="lightblue", ax=ax)
    plt.draw()
    plt.pause(1)


def preparePos(index, x, y, delta):
    if index > len(binary_tree):
        return

    position[index] = (x, y)

    preparePos(index * 2 + 1, x - delta, y - 1, delta / 2)
    preparePos(index * 2 + 2, x + delta, y - 1, delta / 2)


binary_tree = [3, 6, 7, 4, 9, 6, 11, 33]

G = nx.DiGraph()
plt.ion()
fig, ax = plt.subplots()
position = {}
preparePos(0, 0.5, 0.98, 0.01)

print(position)
dfs(0)

plt.ioff()
plt.show()
