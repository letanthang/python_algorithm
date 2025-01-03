import numpy as np
from tensorly.decomposition import parafac
import matplotlib.pyplot as plt
import pandas as pd


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
    tensor = np.zeros((num_time_bins, num_users, num_users), dtype=np.int32)

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
            tensor[t, u, u2] = 1  # Đánh dấu có sự tương tác

        return tensor


np.random.seed(10)
data = process_mooc_to_tensor("mooc_actions.tsv")
data = data + 0.005 * np.random.rand(data.shape[0], data.shape[1], data.shape[2])

data = data[:2, :1000, :1000]
# np.save("tensor_data.npy", data)
# data = np.load("tensor_data.npy")
# det = np.linalg.det(matrix2)
print("Tensor Data Shape:", data.shape)

# Step 2: Thực hiện CP decomposition với rank cố định (ví dụ rank = 3)
rank = 7  # Số cộng đồng giả định
weights, factors = parafac(data, rank=rank, init="random", verbose=0)

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
        print(
            f"Node {i+1} belongs to: {', '.join([f'Community {m+1}' for m in memberships])}"
        )
    else:
        print(f"Node {i+1} does not belong to any community.")

# Step 4: Trực quan hóa bằng biểu đồ scatter plot
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "black",
    "purple",
    "orange",
]  # Màu sắc tương ứng với cộng đồng 1, 2, 3
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
