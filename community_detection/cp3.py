import numpy as np
from tensorly.decomposition import parafac
import matplotlib.pyplot as plt


def import_adjacency_list(file_path):
    matrix = np.zeros((105, 105), dtype=int)
    with open(file_path, "r") as file:
        for line in file:
            node1, node2 = line.split(" ")
            n1 = int(node1.strip())
            n2 = int(node2.strip())
            matrix[n1 - 1, n2 - 1] = 1
            matrix[n2 - 1, n1 - 1] = 1
    return matrix


np.random.seed(42)

# Tensor với giá trị nhị phân và nhiễu nhỏ
tensor_data = import_adjacency_list("dims.txt")
det = np.linalg.det(tensor_data)
print(det)
print("Tensor Data Shape:", tensor_data.shape)

rank = 11
weights, factors = parafac(tensor_data, rank=rank, init="random", verbose=0)

# Ma trận yếu tố cho Mode-1 (node)
node_factors = factors[1]
print("\nNode Factor Matrix:")
print(node_factors)

threshold = 0.2  # Ngưỡng xác định
community_assignments = (node_factors > threshold).astype(int)

print("\nCommunity Memberships (1: Belongs, 0: Does Not Belong):")
node_to_community = {}
for i, node in enumerate(community_assignments):
    memberships = [j for j, value in enumerate(node) if value == 1]
    node_to_community[i] = memberships
    if memberships:
        print(
            f"Node {i+1} belongs to: {', '.join([f'Community {m+1}' for m in memberships])}"
        )
    else:
        print(f"Node {i+1} does not belong to any community.")

colors = ["red", "blue", "green"]  # Màu sắc tương ứng với cộng đồng 1, 2, 3
plt.figure(figsize=(8, 6))

for node, communities in node_to_community.items():
    if communities:  # Node thuộc ít nhất một cộng đồng
        for comm in communities:
            plt.scatter(
                node,
                comm,
                color=colors[comm],
                s=200,
                label=f"Node {node+1}" if comm == communities[0] else "",
            )
    else:  # Node không thuộc cộng đồng nào
        plt.scatter(
            node, -1, color="gray", s=200, label=f"Node {node+1} (No Community)"
        )

# Tuỳ chỉnh biểu đồ
plt.xlabel("Nodes")
plt.ylabel("Communities")
plt.title("Node Membership in Communities")
plt.yticks(
    range(-1, rank), ["No Community"] + [f"Community {i+1}" for i in range(rank)]
)
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", title="Nodes")
plt.grid(True)
plt.show()
