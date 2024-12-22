import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac
import matplotlib.pyplot as plt

# Step 1: Tạo tensor dữ liệu kích thước 2x10x10
np.random.seed(42)

# Tensor với giá trị nhị phân và nhiễu nhỏ
tensor_data = np.array([
    np.random.randint(0, 2, (10, 10)),  # Quan hệ loại 1
    np.random.randint(0, 2, (10, 10))   # Quan hệ loại 2
]) + 0.05 * np.random.rand(2, 10, 10)

print("Tensor Data Shape:", tensor_data.shape)

# Step 2: Thực hiện CP decomposition với rank cố định (ví dụ rank = 3)
rank = 3  # Số cộng đồng giả định
weights, factors = parafac(tensor_data, rank=rank, init='random', verbose=0)

# Ma trận yếu tố cho Mode-1 (node)
node_factors = factors[1]
print("\nNode Factor Matrix:")
print(node_factors)

# Step 3: Xác định node có thuộc cộng đồng nào không
threshold = 0.2  # Ngưỡng xác định
community_assignments = (node_factors > threshold).astype(int)

print("\nCommunity Memberships (1: Belongs, 0: Does Not Belong):")
node_to_community = {}
for i, node in enumerate(community_assignments):
    memberships = [j for j, value in enumerate(node) if value == 1]
    node_to_community[i] = memberships
    if memberships:
        print(f"Node {i+1} belongs to: {', '.join([f'Community {m+1}' for m in memberships])}")
    else:
        print(f"Node {i+1} does not belong to any community.")

# Step 4: Trực quan hóa bằng biểu đồ scatter plot
colors = ['red', 'blue', 'green']  # Màu sắc tương ứng với cộng đồng 1, 2, 3
plt.figure(figsize=(8, 6))

for node, communities in node_to_community.items():
    if communities:  # Node thuộc ít nhất một cộng đồng
        for comm in communities:
            plt.scatter(node, comm, color=colors[comm], s=200, label=f'Node {node+1}' if comm == communities[0] else "")
    else:  # Node không thuộc cộng đồng nào
        plt.scatter(node, -1, color='gray', s=200, label=f'Node {node+1} (No Community)')

# Tuỳ chỉnh biểu đồ
plt.xlabel("Nodes")
plt.ylabel("Communities")
plt.title("Node Membership in Communities")
plt.yticks(range(-1, rank), ['No Community'] + [f'Community {i+1}' for i in range(rank)])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Nodes")
plt.grid(True)
plt.show()