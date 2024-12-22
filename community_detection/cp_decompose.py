import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac
import matplotlib.pyplot as plt

# Step 1: Create a toy multi-relational network as a tensor
# 3D tensor (e.g., 4 nodes, 4 nodes, and 2 relationship types)
tensor_data = np.array([
    # Relation type 1 (e.g., friendship)
    [
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]
    ],
    # Relation type 2 (e.g., professional connection)
    [
        [1, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 1]
    ]
]) + 0.1 * np.random.rand(2, 4, 4)

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