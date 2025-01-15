import numpy as np
import networkx as nx
from tensorly.decomposition import parafac
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


# Load the MOOC dataset
def process_mooc_to_tensor(filepath):
    df = pd.read_csv(
        filepath,
        sep="\t",
        names=["ACTIONID", "USERID", "TARGETID", "TIMESTAMP"],
        skiprows=2,
    )

    df.drop("ACTIONID", axis=1, inplace=True)

    df["TIMESTAMP"] = df["TIMESTAMP"].astype(int)
    df["USERID"] = df["USERID"].astype(int)
    df["TIME_BIN"] = df["TIMESTAMP"] // (
        3600 * 24 * 7
    )  # Change to your desired time granularity

    df.head(5)

    # Xác định số lượng User
    num_users = df["USERID"].max() + 1

    # Xác định số lượng thời gian (time bins)
    num_time_bins = df["TIME_BIN"].max() + 1

    # Tạo tensor (Time x User x User) và khởi tạo bằng 0
    tensor = np.zeros((num_users, num_users, num_time_bins), dtype=np.int32)

    # Lặp qua từng hàng trong dataframe và cập nhật tensor
    for _, row in df.iterrows():
        t = row["TIME_BIN"]  # Time bin
        u = row["USERID"]  # User ID
        f = row["TARGETID"]  # Feature ID

        # Tìm các người dùng khác đã tương tác cùng tính năng tại thời điểm này
        interacted_users = df[
            (df["TIME_BIN"] == t) & (df["TARGETID"] == f) & (df["USERID"] != u)
        ]["USERID"].values

        # Cập nhật các cặp người dùng tương tác trong tensor
        for u2 in interacted_users:
            tensor[u, u2, t] = 1  # Đánh dấu có sự tương tác

        return tensor


np.random.seed(10)
# crop dimensions
t = 5
# n = 7047
n = 1500
data = process_mooc_to_tensor("mooc_actions.tsv")
graph_data = data[:n, :n, :t][0]
data = data + 0.005 * np.random.rand(data.shape[0], data.shape[1], data.shape[2])
data = data[:n, :n, :t]
# np.save("tensor_data.npy", data)
# data = np.load("tensor_data.npy")
# det = np.linalg.det(matrix2)
print("Tensor Data Shape:", data.shape)

# Step 2: Thực hiện CP decomposition với rank cố định (ví dụ rank = 3)
rank = 3  # Số cộng đồng giả định
weights, factors = parafac(data, rank=rank, init="random", verbose=0)

# Ma trận yếu tố cho Mode-1 (node)
node_factors = factors[0]
# Step 3: Xác định node có thuộc cộng đồng nào không
kmeans = KMeans(n_clusters=3)  # Giả sử có 3 cộng đồng
user_clusters = kmeans.fit_predict(node_factors)


G = nx.Graph()
# In kết quả phân nhóm
print("User clusters:")
node_colors = []
for user_id, cluster in enumerate(user_clusters):
    G.add_node(user_id)
    node_colors.append(cluster)
    print(f"User {user_id} belongs to cluster {cluster}")

nx.draw(G, node_color=node_colors, with_labels=False, node_size=10, cmap=plt.cm.rainbow)
plt.show()
