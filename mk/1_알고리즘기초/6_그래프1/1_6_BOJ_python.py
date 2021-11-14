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
sys.setrecursionlimit(111111)


def next_(index):
    global visited_num
    visited_YN[index] = True
    temp.append(index)
    x = nums[index]

    if visited_YN[x]: #
        if x in temp: # 여기 x부분 틀렸었음
            visited_num = visited_num + temp[temp.index(x):] ### 여기 x부분 틀렸었음
            print(visited_num)
        return
    else:
        next_(x)


for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited_YN = [True] + [False for i in range(n)]
    visited_num = []
    for i in range(1, n+1):
        if not visited_YN[i]:
            temp = []
            next_(i)
    print(n-len(visited_num))


# 2667 : 단지번호 붙이기
def dfs(x, y):
    global house
    if x >= len(nums[0]) or x < 0 or y >= len(nums) or y<0:
        return
    if nums[x][y] == 1:
        nums[x][y] = 0
        house += 1
        bfs(x + 1, y)
        bfs(x, y - 1)
        bfs(x - 1, y)
        bfs(x, y + 1)
        return True
    else:
        return

T = int(input(""))
nums = []
for i in range(T):
    nums.append(list(map(int, input(""))))

count = []
for i in range(len(nums)):
    for j in range(len(nums[0])):
        if nums[i][j] == 1:
            house = 0
            if dfs(i, j) == True:
                count.append(house)
print(len(count))
count.sort()
for i in count:
    print(i)


# 4963 : 섬의 개수
def bfs(x, y):
    global mymap, w, h
    if x > h or x < 0 or y > w or y < 0:
        return
    if mymap[x][y] == 1:
        mymap[x][y] = 0
        bfs(x + 1, y)
        bfs(x, y - 1)
        bfs(x - 1, y)
        bfs(x, y + 1)
        bfs(x - 1, y + 1)
        bfs(x + 1, y + 1)
        bfs(x - 1, y - 1)
        bfs(x + 1, y - 1)
        return True
    else:
        return

while True:
    w, h = list(map(int, input().split(" ")))
    if (w, h) == (0, 0):
        break
    mymap = [[0 for i in range(w+1)]]
    for i in range(h):
        mymap.append([0]+list(map(int, input("").split(" "))))
    count = 0
    for i in range(1, h+1):
        for j in range(1, w+1):
            if mymap[i][j] == 1:
                if bfs(i, j) == True:
                    count += 1
    print(count)


# 2178 미로 탐색
from collections import deque

N, M = list(map(int, input().split(" ")))

list1 = [[0 for i in range(M+1)]]
for i in range(N):
    list1.append([0]+list(map(int, list(input()))))

q = deque()
q.append([1, 1])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 1 or nx > N or ny < 1 or ny > M:
            continue
        if list1[nx][ny] == 1:
            list1[nx][ny] = list1[x][y]+1
            q.append([nx, ny])
print(list1[N][M])

# 7576 : 토마토
from collections import deque
from functools import reduce

M, N = list(map(int, input().split(" ")))

list1 = [[0 for i in range(M+1)]]
count1 = 0
index1 = []

for i in range(N):
    inputlist = list(map(int, list(map(int, input().split(" ")))))
    for j in range(len(inputlist)):
        if inputlist[j] == 1:
            count1 += 1
            index1.append([i+1, j+1])
    list1.append([0]+inputlist)

qs = []
for i in index1:
    q = deque()
    q.append(i)
    qs.append([q, deque()])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while reduce(lambda x, y : x+y, reduce(lambda x, y : x+y, qs)):
    for q in qs:
        print(q, len(q[0]))
        while len(q[0]) > 0:
            x, y = q[0].popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 1 or nx > N or ny < 1 or ny > M:
                    continue
                if list1[nx][ny] == 0:
                    list1[nx][ny] = list1[x][y] + 1
                    q[1].append([nx, ny])
            q[0] = q[1]
            q[1] = deque()
        '''for i in qs:
            print(i)
    for i in list1[1:]:
        print(i[1:])'''
    print("---")
