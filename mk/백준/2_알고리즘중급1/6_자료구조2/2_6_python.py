# 1717 집합의 표현
'''
자료구조 : 트리 / 루트노드로 집합 구분
'''

'''
# 틀린 원래 코드
# find 할 때 parents 리스트를 부모노드가 아닌 루트노드로 업데이트 안 하면 시간 초과됨
# if yn==0 부분 조금 틀림

n, m = map(int, input().split())
parents = [i for i in range(n+1)]


def find_root(child):
    while parents[child] != child:
        child = parents[child]
    return child


for i in range(m):
    yn, a, b = map(int, input().split())
    if yn == 0:
        parents[max(find_root(max(a, b)), min(a, b))] = min(find_root(max(a, b)), min(a,b))
    else:
        if find_root(a) != find_root(b):
            print('NO')
        else:
            print('YES')
'''

# union-find 알고리즘
n, m = map(int, input().split())
parents = [i for i in range(n+1)]


def find_root(child): # find
    x_child = child
    while parents[child] != child:
        child = parents[child]
    parents[x_child] = child
    return child


for i in range(m):
    yn, a, b = map(int, input().split())
    if yn == 0:
        # union
        parents[max(find_root(a), find_root(b))] = min(find_root(a), find_root(b))
    else:
        if find_root(a) != find_root(b):
            print('NO')
        else:
            print('YES')


# 2606 바이러스
from collections import deque

N = int(input())
num = int(input())
visited = [False] * (N+1)
connected = [[] for i in range(N+1)]
for i in range(num):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

queue = deque([1])
visited[1] = True

while queue:
    out = queue.popleft()
    for i in connected[out]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True

print(visited.count(True)-1)

