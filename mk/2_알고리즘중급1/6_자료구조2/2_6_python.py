# 1717 집합의 표현
'''
자료구조 : 트리 / 루트노드로 집합 구분
'''
n, m = map(int, input().split())
lists = []
indexes = [0 for i in range(n+1)]





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

