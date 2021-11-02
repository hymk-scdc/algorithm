# 1260 : DFS와 BFS
from collections import deque

N, M, V = list(map(int, input().split(" ")))
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = list(map(int, input().split(" ")))
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (N+1)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, V, [False] * (N+1))
print("")
bfs(graph, V, [False] * (N+1))


# 11724 : 연결 요소의 개수
