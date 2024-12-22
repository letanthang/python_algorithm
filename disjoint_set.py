
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Each element is initially its own parent
        self.rank = [0] * n           # Rank for each element is initially zero

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def print_all(self):
        print("Parent Array:", self.parent)
        print("Rank Array:", self.rank)
        print("----------------------------")

    def get_sets(self):
        map_sets = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root in map_sets:
                map_sets[root].append(i)
            else:
                map_sets[root] = [i]

        return list(map_sets.values())

    def print_sets(self):
        sets = self.get_sets()
        for s in sets:
            print("Root:", s[0], "Members:", s)