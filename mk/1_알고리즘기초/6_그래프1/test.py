n = int(input())
graph = []
for i in range(n) :
    graph.append(list(map(int, input().split())))

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.popleft()
        for i in range(4) : # 상하좌우
            nx, ny = x+dx[i], y+dy[i]

            if nx > -1 and nx < n and ny >-1 and ny < n :
                if graph[nx][ny] == 0 :
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y]+1
                elif graph[nx][ny] > graph[x][y]+1 :
                    queue.append((nx, ny))
                    graph[nx][ny] = min(graph[nx][ny], graph[x][y]+1)
                # elif graph[nx][ny] == graph[x][y]+1 :
                #     result.append(graph[nx][ny])


result = []

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            bfs(i,j)