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
'''
시간초과
'''
import sys

def next_(index):
    global visited_num
    #print('**index', index)
    if visited_YN[index] == 0:
        visited_YN[index] = 1
        temp.append(index)
        #print(visited_YN)
        #print(temp)
        #print("--")
        next_(nums[index])
    elif visited_YN[index] == 1:
        #print('index', index)
        if index in temp:
            visited_num = visited_num + temp[temp.index(index):]
            for i in visited_num:
                visited_YN[i] = 2
        return
        #print(visited_YN)
        #print(temp)
        #print('visited_num', visited_num)
        #print('------')
    #else:
     #   temp = []
      #  print("---")


for T in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    nums = [0] + list(map(int, sys.stdin.readline().strip().split(" ")))
    visited_YN = [0 for i in range(n+1)]
    visited_num = []
    temp = []
    for i in range(1, n+1):
        if visited_YN[i] == 0:
            temp = []
            next_(i)
            #print('---')
            #print('---')
    print(n-len(visited_num))

'''
다시..
'''
import sys


def next_(index):
    global visited_num
    visited_YN[index] = 1
    temp.append(index)
    if visited_YN[nums[index]] == 1:
        if index in temp:
            visited_num = visited_num + temp[temp.index(index):]
        return
    else:
        next_(nums[index])


for T in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    nums = [0] + list(map(int, sys.stdin.readline().rstrip().split(" ")))
    visited_YN = [0 for i in range(n+1)]
    visited_num = []
    for i in range(1, n+1):
        if visited_YN[i] == 0:
            temp = []
            next_(i)
    print(n-len(visited_num))
