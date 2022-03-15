# 11437 LCA
import sys
sys.setrecursionlimit(100000)

N = int(input())
parents = [0 for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
depth_yn = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def get_depth(node, depth_):
    depth_yn[node] = 1
    depth[node] = depth_
    for child in graph[node]:
        if depth_yn[child] == 0:
            parents[child] = node
            get_depth(child, depth_+1)


get_depth(1, 0)


def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parents[a]
        else:
            b = parents[b]
    while a != b:
        a = parents[a]
        b = parents[b]
    return a


M = int(input())
answer = []
for i in range(M):
    a, b = map(int, input().split())
    answer.append(lca(a, b))
for i in answer:
    print(i)



# 11437 LCA 2
