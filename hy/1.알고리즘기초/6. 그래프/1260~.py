# 음료수 얼음 얼려먹기

# 데이터 담기
n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # cf. str은 iterable


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        print(x,y)
        return False
    # 방문처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        print("여기가 트루야" , x, y)
        return True
    return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)


# 재귀함수 연습
def pr(i) :
    if i >= 10 :
        print(i, "넘음")
    else :
        print(i,"안넘음")
        pr(i+1) # 여기서 1 ~ 10 까지 갔음
        print(i,"돌아와") # 9 ~ 1 까지 다시 돌아감
        pr(i+2) # 근데 9 -> 11 //-> 8 -> 10 //-> 7 -> 9 -> 10 -> 9 -> 11 //


# 미로탈출
101010
111111
000001
111111
111111

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
#
# x, y, cnt = 0, 0 ,1
#
# def dfs(x, y, cnt):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         print(x,y)
#         return False
#     # 방문처리
#     if graph[x][y] == 1:
#         graph[x][y] = 0
#         dfs(x-1, y, cnt)
#         dfs(x, y-1, cnt)
#         dfs(x+1, y, cnt)
#         dfs(x, y+1, cnt)
#         cnt+=1
#         return cnt
#     return False

def bfs(x,y) :
    # 큐에 노드 쌓기
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 때까지
    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    return graph[n-1][m-1]

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]




# 1260 DFS와 BFS


'''
리스트에 곱하기로 생성하면 하나만 바꿔도 다 바뀌는 문제 발생하니깐 
list comprehension으로 해결해야 한다. 
'''
n, m , v = map(int, input().split())
graph = [[] for _ in range(m+1)]

for _ in range(m) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()



# dfs
def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)


# bfs
def bfs(graph, v , visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i]:
            visited[i] = True
            print(i, end=' ')
    for i in graph[v] :
        bfs(graph, i, visited)









# 답
visited = [False for i in range(n+1)]
dfs(graph, v, visited)
visited = [False for i in range(n+1)]
print('')
print(v, end = ' ')
bfs(graph, v , visited)










