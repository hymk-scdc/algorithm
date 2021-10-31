# DFS / BFS

# [(이코테 2021 강의 몰아보기) 3. DFS & BFS](https://www.youtube.com/watch?v=7C9RgOcvkvo&t=24s)

'''
재귀함수
- 팩토리얼
- 최대공약수 계산
'''

'''
DFS 소스코드 예제
'''
# 해당 인덱스 번호의 노드의 인접 노드가 리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 정보
visited = [False] * 9


# dfs 함수
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = '')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# dfs 함수 호출
dfs(graph, 1, visited)


'''
BFS 소스코드 예제
'''
from collections import deque

# 해당 인덱스 번호의 노드의 인접 노드가 리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 정보
visited = [False] * 9


# bfs 함수
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 떄까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end='')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# bfs 함수 호출
bfs(graph, 1, visited)


'''
문제 풀이
'''

# 음료수 얼려 먹기
from collections import deque

N, M = list(map(int, input().split(" ")))

list1 = []
for i in range(N):
    list1 = list1+list(map(int, input()))

qq = deque()
cnt = 0
for i in range(N*M):
    if list1[i] == 1:
        continue
    else:
        qq.append(i)
        list1[i] = 1
        while qq:
            v = qq.popleft()
            for j in [-1, 1, M, -M]:
                if (v + j < 0) or (v % M == 0 and j == -1) or (v % M == M-1 and j == 1) or (v+j >= N*M):
                    continue
                else:
                    if list1[v+j] == 0:
                        qq.append(v + j)
                        list1[v+j] = 1
        cnt += 1

print(cnt)


# 미로 탈출
'''
내꺼 - 미완성
무한 루프 원인 - 148 line
'''
from collections import deque

N, M = list(map(int, input().split(" ")))

list1 = []
for i in range(N):
    list1.append(list(map(int, input())))

qq = deque()
qq.append([0, 0])

while qq:
    print(".....")
    v = qq.popleft()
    if [v[0], v[1]] == [N - 1, M - 1]:
        break
    for k in [1, -1]:
        if (v[0] + k >= 0) and (v[0] + k < N) and (v[1] + k >= 0) and (v[1] + k < M):
            # != 0로 했을 때 무한루프였음
            if list1[v[0] + k][v[1]] == 1:
                qq.append([v[0] + k, v[1]])
                list1[v[0] + k][v[1]] = list1[v[0]][v[1]] + 1

            if list1[v[0]][v[1] + k] == 1:
                qq.append([v[0], v[1] + k])
                list1[v[0]][v[1] + k] = list1[v[0]][v[1]] + 1



'''
해설
'''
from collections import deque

n, m = list(map(int, input().split(" ")))

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))
