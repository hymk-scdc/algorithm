# 2294 동전 2

n, k = map(int, input().split())

results = [0 for i in range(k+1)]
coins = []

for i in range(n):
    coin = int(input())
    coins.append(coin)

if max(coins) > k:
    results = results + [0 for i in range(max(coins)-k)]

for i in coins:
    results[i] = 1

for i in range(min(coins)):
    results[i] = -1

for target in range(1, k+1):
    if (results[target] != 1) and (results[target] != -1):
        compare = []
        for coin in coins:
            if target-coin > 0:
                compare.append(results[target-coin])

        if max(compare) == -1:
            results[target] = -1
        else:
            compare = list(filter(lambda x: x != -1, compare))
            results[target] = min(compare) + 1

print(results[k])


# 1520 내리막길
'''
1. 맞지만 시간초과
'''
from collections import deque

M, N = list(map(int, input().split()))
maps = []
for i in range(M):
    maps.append(list(map(int, input().split())))

visited = deque([[0, 0]])

x, y = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0

while (visited):
    x, y = visited.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if (nx >= M or ny >= N or nx < 0 or ny < 0):
            continue
        if maps[x][y] > maps[nx][ny]:
            visited.append([nx, ny])

    if (x, y) == (M-1, N-1):
        cnt += 1

print(cnt)



'''
2. visited 쓴 경우 - 틀리게 나옴, 아마 잔가지 뻗어나온 거에서 또 뻗어나온 경우 때메 틀린 것 같음
반례는
9 4 3
8 5 2
7 6 1
정답:6
'''
from collections import deque

M, N = list(map(int, input().split()))
maps = []
for i in range(M):
    maps.append(list(map(int, input().split())))

queues = deque([[0, 0]])
visited = [0 for i in range(M*N)]

x, y = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0

while (queues):
    x, y = queues.popleft()
    #print('x',x, 'y', y, '기준')
    for i in range(4):
        #print(x, x + dx[i], y, y + dy[i])
        nx, ny = x+dx[i], y+dy[i]
        #print('nx', nx, ', ny', ny)
        if (nx >= M or ny >= N or nx < 0 or ny < 0):
            continue
        if maps[x][y] > maps[nx][ny]:
            if visited[N*nx+ny] == 1:
                cnt += 1
            else:
                visited[N*nx+ny] = 1
                queues.append([nx, ny])
            #print(queues)
    #print('--------')

    if (x, y) == (M-1, N-1):
        cnt += 1

print(cnt)


'''
dp로 혼자 해보기0
'''