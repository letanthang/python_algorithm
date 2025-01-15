import math
import random
from disjoint_set import DisjointSet


def karger(edges, vertices, try_num):
    es = edges.copy()
    ds = DisjointSet(len(vertices))
    while len(ds.get_sets()) > 2:
        index = random.randint(0, len(es) - 1)
        u, v = es.pop(index)

        # print("union edge:", u, v)
        ds.union(vertices.index(u), vertices.index(v))
        es = remove_self_loops(es, vertices, ds)

    print(es)
    print(get_ds_value(ds, vertices))
    return es


def remove_self_loops(edges, vertices, ds):
    return [
        (u, v)
        for u, v in edges
        if not ds.is_connected(vertices.index(u), vertices.index(v))
    ]


def get_vertices(edges):
    vertices = set(u for edge in edges for u in edge)
    return vertices


def get_ds_value(ds, vertices):
    sets = ds.get_sets()
    result = []
    for s in sets:
        result.append(set(vertices[i] for i in s))
    return result


edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 6)]
vertices = list(get_vertices(edges))

try_num = int(len(vertices) ** 2 * math.log(len(vertices)))
print("try_num:", try_num)

result = []
for i in range(try_num):
    result.append(karger(edges, vertices, try_num))

min_cut = min(result, key=lambda x: len(x))

print("try_num", try_num, "min_cut", min_cut)
