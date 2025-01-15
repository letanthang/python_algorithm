import networkx as nx
import community  # Louvain method (python-louvain)

# Create a sample graph
G = nx.read_edgelist("107.edges", nodetype=int)

# Apply the Louvain method for community detection
partition = community.best_partition(G)

# Print the partition (community assignment)
# print("Community assignments:", partition)

# Calculate the modularity score of the partition
modularity_score = community.modularity(partition, G)
print("Modularity score:", modularity_score)
print(len(set(partition.values())))
adjacency_matrix = nx.to_numpy_array(G)
print(adjacency_matrix)

# Draw the graph with community colors
import matplotlib.pyplot as plt

# Generate a list of community colors
node_colors = [partition[node] for node in G.nodes()]

# Draw the graph with nodes colored by their community
nx.draw(G, node_color=node_colors, with_labels=False, cmap=plt.cm.rainbow)
plt.show()
