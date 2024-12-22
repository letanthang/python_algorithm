import matplotlib.pyplot as plt
import networkx as nx

edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]

G = nx.Graph()
plt.ion()
fig, ax = plt.subplots()

def update(G):
    ax.clear()
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', ax=ax)
    plt.draw()
    plt.pause(1)

def preparePos():
    all_nodes = set(node for edge in edges for node in edge)
    pos = nx.spring_layout(list(all_nodes))

    return pos

pos = preparePos()
for edge in edges:
    G.add_edge(*edge)
    update(G)

plt.ioff()
plt.show()