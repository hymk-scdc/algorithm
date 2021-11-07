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
N, M = list(map(int, input().split(" ")))
graph = [[] for i in range(N+1)]
for i in range(M):
    u, v = list(map(int, input().split(" ")))
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

def dfs(graph, visited, start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, visited, i)

visited = [False for i in range(N+1)]
count = 0

for i in range(1, N+1):
    if visited[i] == False:
        dfs(graph, visited, i)
        count += 1

print(count)


# 1707 : 이분 그래프
'''
visited : 0(미방문) 1(집합1) -1(집합2)
'''
from collections import deque


def bfs(graph, visited):
    for i in range(1, len(graph)):
        if visited[i] == 0:
            queue = deque([i])
            visited[i] = 1
            while queue:
                v = queue.popleft()
                for i in graph[v]:
                    if visited[i] == 0:
                        queue.append(i)
                        visited[i] = visited[v] * (-1)
    return visited


def answer():
    V, E = list(map(int, input().split(" ")))
    graph = [[] for i in range(V + 1)]
    for j in range(E):
        u, v = list(map(int, input().split(" ")))
        graph[u].append(v)
        graph[v].append(u)

    visited = bfs(graph, [0] * (V + 1))

    for i in range(V+1):
        for j in range(len(graph[i])):
            graph[i][j] = visited[graph[i][j]]
    for i in graph:
        if len(set(i)) > 1:
            return 'NO'
    return 'YES'


K = int(input(""))
for i in range(K):
    print(answer())


# 10451 : 순열 사이클
def dfs(graph, v, visited):
    if visited[v] == False:
        visited[v] = True
        dfs(graph, graph[v], visited)

T = int(input(""))

for k in range(T):
    N = int(input(""))
    graph = [0] + list(map(int, input("").split(" ")))
    visited = [False for i in range(N+1)]
    count = 0

    for i in range(1, N+1):
        if visited[i] == False:
            dfs(graph, i, visited)
            count += 1

    print(count)


# 2331 : 반복수열
'''
그래프 아님
'''
A, P = list(input("").split(" "))
nums = [A]

while True:
    new = sum(list(map(lambda x: int(x)**int(P), nums[-1])))
    if str(new) in nums:
        nums = nums[:nums.index(str(new))]
        break
    else:
        nums.append(str(new))

print(len(nums))


# 9466 : 텀 프로젝트
