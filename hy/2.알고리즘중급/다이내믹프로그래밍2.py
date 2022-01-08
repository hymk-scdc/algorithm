# 동전2

n , k = map(int,input().split())

coins = []

for _ in range(n) :
    coins.append(int(input()))

coins.sort(reverse=True)

def coincnt(coins,k, start) :
    cnt = 0
    s, r = 0, None
    while (r != 0) and (start != n) :
        coin = coins[start]
        s = k//coin # 몫
        r = k%coin # 나머지
        k = r # 남은 값어치
        cnt += s
        start += 1
    if r != 0 :
        cnt = -1
    return cnt


result = 10001
for i in range(n) :
    count = coincnt(coins,k,i)
    if count != -1 :
        result = min(result, count)


if result == 10001 :
    print(-1)
else :
    print(result)

#
# n , k = map(int,input().split())
#
# coins = []
#
# for i in range(n) :
#     coins.append(int(input()))
#
# coins.sort(reverse=True)
#
#
# def coincnt(coins,k, start) :
#     cnt = 0
#     s, r = 0, None
#     try :
#         while r != 0 or start != n :
#                 coin = coins[start]
#                 s = k//coin # 몫
#                 r = k%coin # 나머지
#                 k = r # 남은 값어치
#                 cnt += s
#                 start += 1
#     except :
#         cnt = -1
#     return cnt
#
#
#
# result = 10001
# for i in range(n) :
#     count = coincnt(coins,k,i)
#     if count != -1 :
#         result = min(result, count)
#
#
# if result == 10001 :
#     print(-1)
# else :
#     print(result)



n, k = map(int,input().split())

coins = []

for i in range(n) :
    coins.append(int(input()))

coins.sort()
result = [10001] * (k+1)
result[0] = 0

for coin in coins :
    for j in range(coin, k+1) :
        result[j] = min(result[j], result[j-coin]+1)

if result[k] == 10001 :
    print(-1)
else :
    print(result[k])


# 내리막 길
'''시간초과'''
m, n = map(int,input().split())

graph = []

for i in range(m) :
    graph.append(list(map(int,input().split())))

dp = [[[] for _ in range(n)] for _ in range(m) ]
result = 1
def dfs(x,y) :
    global result

    if x == m-1 and y == n-1 :
        return
    dx = [0,0,-1,1] # 상하좌우
    dy = [-1,1,0,0]

    for i in range(4) :
        cx, cy = x+dx[i], y+dy[i]
        if cx < 0 or cx >= m or cy <0 or cy >= n :
            continue
        else :
            if graph[cx][cy] < graph[x][y] and (cx,cy) not in dp[x][y]:
                dp[x][y].append((cx,cy)) # 본인보다 작은 애들 담아둠


    if len(dp[x][y]) == 0 :
        result -= 1
    elif len(dp[x][y]) > 1 :
        result += (len(dp[x][y])-1)

    for nx,ny in dp[x][y] :
        dfs(nx,ny)

dfs(0,0)

print(result)

#-------------------------
import sys

m, n = map(int,sys.stdin.readline().split())

graph = []

for i in range(m) :
    graph.append(list(map(int,sys.stdin.readline().split())))

cnt = 0
def dfs(x,y) :
    global cnt
    if x == m-1 and y == n-1 :
        cnt +=1
        return

    dx = [0, 0, -1, 1]  # 상하좌우
    dy = [-1, 1, 0, 0]

    for i in range(4):
        cx, cy = x + dx[i], y + dy[i]
        if cx < 0 or cx >= m or cy <0 or cy >= n :
            continue
        else :
            if graph[cx][cy] >= graph[x][y] :
                continue
            else :
                # print(graph[x][y], graph[cx][cy], cx,cy)
                dfs(cx,cy)

    return cnt

print(dfs(0,0))


import sys
m, n = map(int,sys.stdin.readline().split())

graph = []

for i in range(m) :
    graph.append(list(map(int,sys.stdin.readline().split())))


def finddp(x,y) :
    dx = [0, 0, -1, 1]  # 상하좌우
    dy = [-1, 1, 0, 0]

    for i in range(4):
        cx, cy = x + dx[i], y + dy[i]
        if cx < 0 or cx >= m or cy < 0 or cy >= n:
            continue
        else:
            if graph[cx][cy] > graph[x][y] :
                if visited[cx][cy] == 0 : # 자기보다 큰 애가 아직 방문 안했으면 걔부터 구하게 함
                    finddp(cx,cy)
                    dp[x][y] += dp[cx][cy]

                else :
                    dp[x][y] += dp[cx][cy]
    visited[x][y] = 1
    return

dp = [[0 for _ in range(n)] for _ in range(m) ]
visited = [[0 for _ in range(n)] for _ in range(m) ]


visited[0][0] = 1
dp[0][0] = 1

for i in range(m) :
    for j in range(n) :
        if i == 0 and j == 0 :
            pass
        else :
            if visited[i][j] == 0 :
                finddp(i,j)
print(dp[m-1][n-1])
