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

틀린 답이랍니다아 
'''
n, m , v = map(int, input().split())
graph = [[] for _ in range(n+1)]

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


# # bfs
# def bfs(graph, v , visited, visited2) :
#     visited[v] = True
#     visited2[v] = True
#     for i in graph[v] :
#         if not visited[i]:
#             visited[i] = True
#             print(i, end=' ')
#     for i in graph[v] :
#         if not visited2[i] :
#             visited2[i] = True
#             bfs(graph, i, visited, visited2)

#
# from collections import deque
# def bfs(graph, v, visited) :
#
#     visited[v] = True
#     temp = []
#     for i in graph[v] :
#         if not visited[i] :
#             visited[i] = True
#             print(i, end = ' ')
#             temp.append(i)
#         for j in temp :
#             bfs(graph,j,visited)


# 새로운 BFS

from collections import deque

def bfs(graph, start, visited) :
    visited[start] = True
    queue = deque([start])

    while queue :
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True




# 답
visited = [False for i in range(n+1)]
dfs(graph, v, visited)
print('')
visited = [False for i in range(n+1)]
bfs(graph, v , visited)




# 11724 연결 요소의 개수

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    graph[u].sort()
    graph[v].sort()


visited = [False for _ in range(n+1)]

def bfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            visited[i] = True
            # print("v---->", v, "i----->", i)
            bfs(graph, i, visited)
    # return True

result = 0
for v in range(1,n+1) :
    if visited[v] == False :
        bfs(graph, v, visited)
        result +=1

print(result)


# 1707 이분 그래프
from collections import deque

def bi_graph(graph, start , visited) :
    queue = deque([start]) # 큐를 만듦
    visited[start] = 1 # 처음 시작은 방문함
    while queue : # 큐에 담긴 애들 다 살펴보기
        v = queue.popleft() # 살펴본 애들은 빼기

        for i in graph[v] : # 살펴본 아이와 인접한 애들 다 연결하기
            if not visited[i] :
                queue.append(i)
                visited[i] = -visited[v]
            else:
                if visited[i] == visited[v] :
                    return False
    return True



k = int(input())

for _ in range(k) :
    v, e = map(int,input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]

    for _ in range(e) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    result = True
    for i in range(1,v+1) :
        if visited[i] == False :
            if not bi_graph(graph, i, visited) :
                result = False
                break
    print("YES" if result else "NO")

'''
이 코드 진짜 이상함.. 위랑 크게 다른 거 없는데 
from collections import deque
def bi_graph(graph, start , visited) :
    queue = deque([start]) # 큐를 만듦
    visited[start] = 0 # 처음 시작은 방문함
    count = 0
    while queue : # 큐에 담긴 애들 다 살펴보기
        v = queue.popleft() # 살펴본 애들은 빼기
        count +=1
        for i in graph[v] : # 살펴본 아이와 인접한 애들 다 연결하기
            if not visited[i] :
                queue.append(i)
                visited[i] = count%2
            else:
                if visited[i] != count%2 :
                    return False
    return True
k = int(input())
for _ in range(k) :
    v, e = map(int,input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]
    for _ in range(e) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    result = True
    for i in range(1,v+1) :
        if visited[i] == False :
            if not bi_graph(graph, i, visited) :
                result = False
                break
    print("YES" if result else "NO")
    
    '''

# 10451 순열 사이클

def cycle(graph, v, visited) :
    visited[v] = True
    # i = graph[v]
    # if not visited[i] :
        # visited[i] = True
        # cycle(graph, i, visited)
    # return True
    cycle(graph, graph[v], visited)


T = int(input())

for _ in range(T) :
    N = int(input())
    graph = [''] + list(map(int, input().split()))
    visited = [False for _ in range(N+1)]
    result = 0
    for i in range(1,N) :
        if not visited[i] :
            # if cycle(graph,i, visited) :
            cycle(graph, i, visited)
            result +=1
    print(result)

# 2331 반복수열

A, P = input().split()
def banbok(A, P, seq) :
    seq.append(int(A))
    visited[int(A)] = 1
    a = list(map(int, list(A)))
    temp = 0
    for i in a :
        temp += i**P
    if visited[temp] == 0 :
        banbok(str(temp), P, seq)

    elif visited[temp] == 1 :
        print(seq.index(temp))
        return


seq = []
visited = [0 for _ in range(236197)]
banbok(A,int(P),seq)


'''
재귀함수가 벗겨지면서 계속 return None을 하고 있어서, 
마지막 return None 을 반환하게 되는 거였음 

=> 해결방법 : global 선언 

def banbok(A, P, seq) :
    seq.append(int(A))
    visited[int(A)] = 1
    a = list(map(int, list(A)))
    temp = 0
    for i in a :
        temp += i**P
    if visited[temp] == 0 :
        banbok(str(temp), P, seq)
    elif visited[temp] == 1 :
        print(seq.index(temp))
        return temp
seq = []
visited = [0 for _ in range(236197)]
result = banbok(A,int(P),seq)
print(result)
'''

# 9466 텀 프로젝트
# '''틀린 코드'''
# T = int(input())
#
# for _ in range(T) :
#     n = int(input())
#     graph = [''] + list(map(int, input().split()))
#
#     def dfs(graph, v, visited, first) :
#         global count, result
#         count +=1 # 연결된 애들 개수
#         result = False # 연결 여부
#         visited[v] = True # 방문여부
#         i = graph[v] # 처음 시작 위치 고정
#         if visited[i] == True :
#             if i == first :
#                 result = True
#
#             elif i == graph[i] :
#                 count = 1
#                 result = True
#                 visited[i] = "self"
#
#         elif visited[i] == False :
#             dfs(graph,i, visited, first)
#         return count if result else False
#
#     submit = n
#     answer = False
#
#     visited = [False for _ in range(n + 1)]
#
#
# # '''내가 하고 싶은 것은 visited에서 연결된 애들은 냅두고 연결 안된 애들만 계속 다시 갱신해주고 싶음 '''
#     for i in range(1, n+1) :
#         if answer == False :
#
#             count = 0
#             answer = dfs(graph,i,visited,i)
#             if answer != False :
#                 submit -= answer
#
#         else :
#             if visited2[i] == False :
#                 count = 0
#                 answer = dfs(graph, i, visited2, i)
#                 if answer != False:
#                     submit -= answer
#         print("i는 ", i, "현재의 답은 ", answer )
#
#     print(submit)

'''새로운 코드'''

def bfs(graph, v, visited, first):
    global temp
    visited[v] = 1
    i = graph[v]
    if visited[i] == 0:
        visited[i] = 1
        temp.append(i)
        bfs(graph, i, visited, first)
    if visited[i] == 1:
        if graph[i] == first: # 본인이 본인을 가르킨 경우
            visited[i] = 2
        elif i == first:
            temp.append(i)
            for j in temp:
                visited[j] = 2


import sys
T = int(sys.stdin.readline())

for _ in range(T) :
    n = int(sys.stdin.readline())
    graph = [''] + list(map(int, sys.stdin.readline().split()))

    visited = [0 for _ in range(n+1)]

    for k in range(1, n+1) :
        if visited[k] == 0 :
            temp = []
            bfs(graph, k, visited, k)
        for k in range(1, n+1) :
            if visited[k] == 1 :
                visited[k] = 0

    print(visited.count(0)-1)



# 2667 단지번호붙이기

n = int(input())
graph = []

for _ in range(n) :
   graph.append(list(input()))


def dfs(x,y) :
    global cnt
    if x <= -1 or x >=n or y <= -1 or y >= n :
        return False
    if graph[x][y] == '1' : # 벽이면 return
        graph[x][y] = '0' # 방문처리함
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        cnt+=1
        return True
    return False

result = []
for i in range(n) :
    for j in range(n) :
        if graph[i][j] == '1' :
            cnt = 0
            if dfs(i,j) :
                result.append(cnt)
print(len(result))
result.sort()
for answer in result :
    print(answer)



# 4963 섬의 개수

def dfs(x,y) :
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1 :
        graph[x][y] = 0
        dfs(x-1, y-1)
        dfs(x-1, y)
        dfs(x-1, y+1)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1, y-1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        return True
    return False

while True :
    graph = []
    result = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    for _ in range(h) :
        graph.append(list(map(int, input().split())))

    for i in range(h) :
        for j in range(w) :
            if graph[i][j] == 1 :
                if dfs(i,j) :
                    result +=1
    print(result)


# 2178 미로 탐색
from collections import deque
def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    li_x = [-1,1,0,0]
    li_y = [0,0,-1,1]

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx , ny = x + li_x[i], y + li_y[i]
            if nx != -1 and ny != -1 and nx != n  and ny != m :
                if graph[nx][ny] == 1 :
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y]+1
                elif graph[nx][ny] == 0 :
                    continue
    return graph[n-1][m-1]



n, m = map(int , input().split())
graph = []
for _ in range(n) :
    graph.append(list(map(int, input())))

# graph[0][0] = 2
print(bfs(0,0))



# 7576 토마토

'''입력받을 때 아예 익은 토마토 저장하고 시작'''

m, n = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input().split())))

from collections import deque

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx, ny = x+dx[i], y+dy[i] # 상하좌우
            if nx != -1 and ny != -1 and nx != n and ny != m : # 그래프 내 범위 확인
                if graph[nx][ny] == 0 : # 첫 방문
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1 # 하루 추가
                elif graph[nx][ny] >= 2 : # 이미 방문
                    if graph[nx][ny] > graph[x][y] + 1 : # 여기서 출발하는 게 더 익는 시간이 짧은 경우
                        queue.append((nx,ny))
                        graph[nx][ny] = graph[x][y] + 1



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            bfs(i,j)



day = 1
for i in range(n) :
    if day == 0 :
        break
    for j in range(m) :
        if graph[i][j] == 0 :
            day = 0
            print(-1)
            exit()
        else :
            day = max(day, graph[i][j])

print(day-1)


# 2146 다리 만들기

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
                if graph[nx][ny] == cnt :
                    queue.append((nx,ny))
                    graph[nx][ny] = -1
                elif graph[nx][ny] == 0 :
                    graph[nx][ny] = cnt+1
                    queue.append((nx,ny))

for i in range(n) :
    for j in range(n) :
        if graph[i][j] == 1 :
            bfs(i,j)


