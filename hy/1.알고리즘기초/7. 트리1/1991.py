# 1991
class Node() :
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


# 전위 순회

def pre(node) :
    print(node.data)
    if node.left != None :
        pre(tree[node.left])
    if node.right != None :
        pre(tree[node.right])


def mid(node):
    if node.left != None :
        mid(tree[node.left])
    print(node.data)
    if node.right != None :
        mid(tree[node.right])


def post(node):
    if node.left != None :
        post(tree[node.left])

    if node.right != None :
        post(tree[node.right])
    print(node.data)


n = int(input())
tree = {}

for i in range(n) :
    data, left, right = input().split()

    if left == '.' :
        left = None
    if right == '.' :
        right = None

    tree[data] = Node(data, left, right)

pre(tree[root])
mid(tree[root])


# 11725 트리의 부모찾기
'''이거는 recursion limit 바꿔주면 맞는 답임'''
n = int(input())

tree = [[] for _ in range(n+1)]

for i in range(n-1) :
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0 for _ in range(n+1]

def pre(parent) :
    for i in tree[parent] :
        if parents[i] == 0 :
            parents[i] = parent
            pre(i)
pre(1)

for i in parents[2:] :
    print(i)


'''새로운 방법'''
from collections import deque
n = int(input())

tree = [[] for _ in range(n+1)]

for i in range(n-1) :
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0 for _ in range(n+1)]

def pre(root) :
    queue = deque()
    queue.append(root)

    while queue :
        parent = queue.popleft()
        for i in tree[parent] :
            if parents[i] == 0 :
                parents[i] = parent
                queue.append(i)

pre(1)

for i in parents[2:] :
    print(i)


# 1167 트리의 지름
'''주석처리한 거는 시간초과나서, 최대인 애들만 돌게해서 답 구함'''

# def dfs(start) :
#     for tu in tree[start] :
#         i = tu[0]
#         if visited[i] == 0 :
#             print(i, start)
#             visited[i] = visited[start] + tu[1]
#             dfs(i)



# def bfs(start) :
#     queue = deque()
#     for tem in tree[start] :
#         queue.append(tem)
#     visited[start] = 0
#     while queue :
#         i, len_i = queue.popleft()
#         visited[i] = visited[start] + len_i
#         for tu in tree[i] :
#             j, len_j = tu[0], tu[1]
#             if visited[j] == -1 :
#                 visited[j] = visited[i] + len_j
#                 print(i,j,visited[i], len_j)
#                 queue.append(tu)
    #             print(visited)

from collections import deque
import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n) :
    temp = list(map(int,sys.stdin.readline().split()))
    v = temp[0]
    for i in range(1, len(temp)+1,2) :
        if temp[i] == -1 : break
        tree[v].append([v, temp[i], temp[i + 1]])


def bfs(start) :
    queue = deque()
    visited[start] = 0
    for tu in tree[start]:
        queue.append(tu)
    while queue :
        temp = queue.popleft()
        head ,node, link  = temp[0], temp[1], temp[2] # 연결된 앞, 뒤, 길이
        if visited[node] == -1 :
            visited[node] = visited[head] + link
            for tu in tree[node] : # node에 연결된 애들 다 append
                queue.append(tu)

    return visited.index(max(visited)) # 최대인 애로 다시 돌게..그러면 최대인 애에서 또 최대인 애가 나오겠지



# answer = []
# for j in range(1,n+1) :
#     # visited = [-1 for _ in range(n + 1)]
#     visited = [-1]*(n+1)
#     bfs(j)
    # answer.append(max(visited))

j = 1 # 처음 시작위치
temp2 = [] # 최대라고 나왔던 node들 담는 곳
while True :
    visited = [-1]*(n+1)
    a = bfs(j) # 최대라고 나온 node
    if a in temp2 :
        print(max(visited)) # 만약에 이미 최대라고 나왔던 애라면 굳이 다시 안돌아도 되니 끝
        break
    else :
        temp2.append(a)
        j = a



# 1967 트리의 지름
from collections import deque
n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1) :
    p, c, l = map(int, input().split())
    tree[p].append([p,c,l])
    tree[c].append([c,p,l])


def bfs(start):
    queue = deque()
    visited[start] = 0
    for tu in tree[start]:
        queue.append(tu)
    while queue:
        temp = queue.popleft()
        head, node, link = temp[0], temp[1], temp[2]  # 연결된 앞, 뒤, 길이
        if visited[node] == -1:
            visited[node] = visited[head] + link
            for tu2 in tree[node] :
                queue.append(tu2)

    return visited.index(max(visited))  # 최대인 애로 다시 돌게..그러면 최대인 애에서 또 최대인 애가 나오겠지

j = 1 # 처음 시작위치
temp2 = [] # 최대라고 나왔던 node들 담는 곳
while True :
    visited = [-1]*(n+1)
    a = bfs(j) # 최대라고 나온 node
    if a in temp2 :
        print(max(visited)) # 만약에 이미 최대라고 나왔던 애라면 굳이 다시 안돌아도 되니 끝
        break
    else :
        temp2.append(a)
        j = a

