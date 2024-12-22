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
# Áp dụng ngưỡng để xác định membership
threshold = 0.2  # Ngưỡng xác định
community_assignments = (node_factors > threshold).astype(int)

print("\nCommunity Memberships (1: Belongs, 0: Does Not Belong):")
for i, node in enumerate(community_assignments):
    memberships = [f"Community {j+1}" for j, value in enumerate(node) if value == 1]
    if memberships:
        print(f"Node {i+1} belongs to: {', '.join(memberships)}")
    else:
        print(f"Node {i+1} does not belong to any community.")

# Step 4: Trực quan hóa cộng đồng
plt.figure(figsize=(10, 6))
for i in range(rank):
    plt.bar(range(node_factors.shape[0]), node_factors[:, i], label=f'Community {i+1}')
plt.xlabel('Nodes')
plt.ylabel('Membership Strength')
plt.title('Community Membership Strength for Nodes')
plt.axhline(threshold, color='r', linestyle='--', label='Threshold')
plt.legend()
plt.show()