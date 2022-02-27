# 11438 LCA
import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]


for _ in range(n-1) :
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def set_depth() : # depth 세팅해주기
    queue = deque()
    queue.append(1)
    li_depth[1] = 1

    while queue :
        i = queue.pop()
        for j in graph[i] :
            if li_depth[j]==0 :
                queue.append(j)
                li_depth[j] = li_depth[i]+1


def same_depth(a, b) : # depth 위치 맞춰주기
    if li_depth[a] > li_depth[b] : # 항상 b의 depth가 크도록
        b, a = a, b

    while True :
        if li_depth[b] == li_depth[a] :
            break

        for num in graph[b] :
            if li_depth[num] < li_depth[b] :
                b = num
                break


    return a, b

def findparent(a) :
    for num in graph[a]:
        if li_depth[num] < li_depth[a]:
            return num


def lca(a,b) :
    if a == b :
        return a
    while True :
        ap = findparent(a)
        bp = findparent(b)
        if ap == bp :
            return ap
        else :
            a = ap
            b = bp



li_depth = [0 for _ in range(n+1)]
set_depth()


m = int(sys.stdin.readline())
for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    a, b = same_depth(a,b)
    answer = lca(a,b)
    print(answer)

# lca2
import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]


for _ in range(n-1) :
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def set_depth() : # depth 세팅해주기
    queue = deque()
    queue.append(1)
    li_depth[1] = 1
    dp[1] = [1]
    while queue :
        i = queue.pop()
        for j in graph[i] :
            if li_depth[j]==0 :
                queue.append(j)
                li_depth[j] = li_depth[i]+1
                dp[j] = dp[i] + [j]

def same_depth(a, b) : # depth 위치 맞춰주기
    if li_depth[a] > li_depth[b] : # 항상 b의 depth가 크도록
        b, a = a, b

    while True :
        if li_depth[b] == li_depth[a] :
            break

        for num in graph[b] :
            if li_depth[num] < li_depth[b] :
                b = num
                break


    return a, b

def findparent(a) :
    for num in graph[a]:
        if li_depth[num] < li_depth[a]:
            return num

# def usedp(a,b) :
#     skip = 1
#     while skip*2 <= li_depth[a] :
#         skip = skip * 2
#     minus_skip = skip+1
#     ap = dp[a][-minus_skip]
#     bp = dp[b][-minus_skip]
#
#     if ap != dp :
#         skip
#     return ap


def lca(a,b) :
    if a == b :
        return a
    square = 0
    while True :
        # ap = findparent(a)
        # bp = findparent(b)

        if ap == bp :
            return ap
        else :
            a = ap
            b = bp



li_depth = [0 for _ in range(n+1)]
dp = [[] for _ in range(n+1)]
set_depth()


m = int(sys.stdin.readline())
for _ in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    a, b = same_depth(a,b)
    answer = lca(a,b)
    print(answer)



# 11003 최솟값 찾기
n, l = map(int, input().split())
num = list(map(int,input().split()))
d = num[0]
print(d, end = ' ')
for i in range(1,n) :
    d = min(d, num[i])

'''다시 하기'''
from collections import deque
n, l = map(int, input().split())
num = list(map(int,input().split()))
queue = deque()

for i in range(n) :
    queue.append(num[i])
    if len(queue) > l :
        queue.popleft()
    print(min(queue), end = ' ')

'''다시 하기'''
from collections import deque
n, l = map(int, input().split())
num = list(map(int,input().split()))
queue = deque()

temp = num[0]
for i in range(n) :
    queue.append(num[i])
    temp = min(temp, num[i])
    print(queue)

    if len(queue) > l :
        temp1 = queue.popleft()
        if temp == temp1 :
            temp = min(queue)

    print(temp, end = ' ')

'''다시 하기'''
from collections import deque
n, l = map(int, input().split())
num = list(map(int,input().split()))
queue = deque()

# deque에서 본인보다 큰 애들은 삭제
for i in range(n) :
    new = num[i]

    while queue and queue[-1][1] >= new :
        queue.pop()
    while queue and i - queue[0][0] >= l :
        queue.popleft()
    queue.append((i,new))
    # queue.append(new)
    # idx.append(i)
    print(queue[0][1], end = ' ')




# 2042 구간 합 구하기

n,m,k = map(int,input().split())
num = []
for i in range(n) :
    num.append(int(input()))

for j in range(m+k) :
    a, b, c = map(int,input().split())

    if a == 1 :
        num[b-1] = c
    else :
        print(sum(num[b-1:c]))




