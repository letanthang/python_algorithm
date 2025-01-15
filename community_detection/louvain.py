import networkx as nx
import community  # Louvain method (python-louvain)

# Create a sample graph
G = nx.erdos_renyi_graph(30, 0.1)  # Create a random graph

# Apply the Louvain method for community detection
partition = community.best_partition(G)

# Print the partition (community assignment)
print("Community assignments:", partition)

# Calculate the modularity score of the partition
modularity_score = community.modularity(partition, G)
print("Modularity score:", modularity_score)

# Draw the graph with community colors
import matplotlib.pyplot as plt

# Generate a list of community colors
node_colors = [partition[node] for node in G.nodes()]

# Draw the graph with nodes colored by their community
nx.draw(G, node_color=node_colors, with_labels=True, cmap=plt.cm.rainbow)
plt.show()
