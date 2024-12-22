import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac
import matplotlib.pyplot as plt

# Step 1: Create a toy multi-relational network as a tensor
# 3D tensor (e.g., 4 nodes, 4 nodes, and 2 relationship types)
tensor_data = np.array([
    # Quan hệ loại 1 (giá trị ngẫu nhiên và có cấu trúc)
    np.random.randint(0, 2, (10, 10)),  # Ma trận kết nối nhị phân (0 hoặc 1)
    # Quan hệ loại 2 (giá trị ngẫu nhiên)
    np.random.randint(0, 2, (10, 10))
]) + 0.05 * np.random.rand(2, 10, 10)

print(f"Tensor shape: {tensor_data.shape}")  # (2, 4, 4)

# Step 2: Perform CP decomposition to detect communities
rank = 1  # Number of communities to detect
weights, factors = parafac(tensor_data, rank=rank, init='random')

# Step 3: Analyze the factor matrices
print("\nFactor Matrices:")
for i, factor in enumerate(factors):
    print(f"Mode-{i+1} Factors:\n{factor}")

# Step 4: Visualize community membership for nodes
community_matrix = factors[1]  # Factors along mode-1 (nodes)
print("\nCommunity Membership Matrix (Mode-1 Nodes):")
print(community_matrix)

# Plot community membership
plt.figure(figsize=(8, 5))
for i in range(rank):
    plt.bar(range(community_matrix.shape[0]), community_matrix[:, i], label=f'Community {i+1}')
plt.xlabel('Nodes')
plt.ylabel('Membership Strength')
plt.title('Community Memberships')
plt.legend()
plt.show()