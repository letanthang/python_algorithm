import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Create a toy multi-relational network as a tensor
tensor_data = np.array([
    # Quan hệ loại 1 (giá trị ngẫu nhiên và có cấu trúc)
    np.random.randint(0, 2, (10, 10)),  # Ma trận kết nối nhị phân (0 hoặc 1)
    # Quan hệ loại 2 (giá trị ngẫu nhiên)
    np.random.randint(0, 2, (10, 10))
]) + 0.05 * np.random.rand(2, 10, 10)

print(f"Tensor shape: {tensor_data.shape}")  # (2, 4, 4)

# Step 2: Automatically determine the best rank (number of communities)
def find_best_rank(tensor, max_rank=5):
    silhouette_scores = []
    for rank in range(2, max_rank+1):
        weights, factors = parafac(tensor, rank=rank, init='random', verbose=0)
        community_matrix = factors[1]  # Node-community membership matrix
        
        # Use KMeans clustering to assign communities
        kmeans = KMeans(n_clusters=rank, random_state=42, n_init=10)
        labels = kmeans.fit_predict(community_matrix)
        
        # Calculate silhouette score
        score = silhouette_score(community_matrix, labels)
        silhouette_scores.append(score)
        print(f"Rank {rank}: Silhouette Score = {score:.4f}")
    
    # Rank with the highest silhouette score
    best_rank = np.argmax(silhouette_scores) + 2
    return best_rank, silhouette_scores

best_rank, scores = find_best_rank(tensor_data, max_rank=5)
print(f"\nBest Rank (Number of Communities): {best_rank}")

# Step 3: Perform CP decomposition with the best rank
weights, factors = parafac(tensor_data, rank=best_rank, init='random')
community_matrix = factors[1]  # Factors corresponding to nodes

# Step 4: Use KMeans to assign nodes to communities
kmeans = KMeans(n_clusters=best_rank, random_state=42, n_init=10)
labels = kmeans.fit_predict(community_matrix)

print("\nCommunity Assignments:")
for node, community in enumerate(labels):
    print(f"Node {node+1} belongs to Community {community+1}")

# Step 5: Visualize community memberships
plt.figure(figsize=(8, 5))
for i in range(best_rank):
    plt.bar(range(community_matrix.shape[0]), community_matrix[:, i], label=f'Community {i+1}')
plt.xlabel('Nodes')
plt.ylabel('Membership Strength')
plt.title('Community Memberships')
plt.legend()
plt.show()