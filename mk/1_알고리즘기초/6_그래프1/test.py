m, n = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]  # 상하좌우
            if nx != -1 and ny != -1 and nx != n and ny != m:  # 그래프 내 범위 확인
                if graph[nx][ny] == 0:  # 첫 방문
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1  # 하루 추가
                elif graph[nx][ny] >= 2:  # 이미 방문
                    if graph[nx][ny] > graph[x][y] + 1:  # 여기서 출발하는 게 더 익는 시간이 짧은 경우
                        queue.append((nx, ny))
                        graph[nx][ny] = graph[x][y] + 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(i, j)

day = 1
for i in range(n):
    if day == 0:
        break
    for j in range(m):
        if graph[i][j] == 0:
            day = 0
            break
        else:
            day = max(day, graph[i][j])

print(day - 1)