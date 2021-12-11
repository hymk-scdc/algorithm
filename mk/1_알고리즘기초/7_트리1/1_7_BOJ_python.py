# 1991 : 트리 순회

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


# 전위 순회
def pre_order(node):
    print(node.data, end='')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])


# 중위 순회
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None:
        in_order(tree[node.right_node])


# 후위 순회
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end='')


n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == '.':
        left_node = None
    if right_node == '.':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])


# 11725 : 트리의 부모 찾기
'''
recursion error : import sys; sys.setrecursionlimit(10**5) 추가

import sys
sys.setrecursionlimit(100000)

N = int(input())
childs = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = list(map(int, input().split()))
    childs[a].append(b)
    childs[b].append(a)

parents = [0 for i in range(N+1)]


def parent_pop(parent):
    for child in childs[parent]: # child : 4, 6 / parent : 1
        i = childs[child].index(parent)
        parents[child] = childs[child].pop(i)
        parent_pop(child)
    return

parent_pop(1)
for i in parents[2:]:
    print(i)

'''
''' 
다시 해서 해결
def 문 안의 if문 부분 좀 바꿈
- dfs 풀이임
'''
import sys
sys.setrecursionlimit(100000)

N = int(input())
childs = [[] for i in range(N + 1)]

for i in range(N - 1):
    a, b = list(map(int, input().split()))
    childs[a].append(b)
    childs[b].append(a)

parents = [0 for i in range(N + 1)]


def parent_pop(parent):
    for child in childs[parent]:
        if parents[child] == 0:
            parents[child] = parent
            parent_pop(child)
    return

parent_pop(1)

for i in parents[2:]:
    print(i)


# 1167 : 트리의 지름
'''
# 메모리 초과 - deepcopy 를 방문처리로 고쳐보기

import copy

V = int(input())
graph = [[0 for i in range(V+1)] for _ in range(V+1)]
connect = [[] for i in range(V+1)]
for _ in range(V):
    inputs = list(map(int, input().split(" ")))
    x = inputs[0]
    for i in range(1, len(inputs)-1, 2):
        graph[x][inputs[i]] = inputs[i+1]
        graph[inputs[i]][x] = inputs[i+1]
        connect[x].append(inputs[i])

maxdist_1 = 0

def dfs(start, connect1, maxdist):
    global maxdist_1
    for i in connect1[start]: # i : 1, 4 / start : 3
        connect1[i].remove(start)
        dfs(i, connect1, maxdist + graph[start][i])
        maxdist_1 = max(maxdist + graph[start][i], maxdist_1)

    return maxdist_1

result = 0
for i in range(1, V+1):
    connect1 = copy.deepcopy(connect)
    result = max(result, dfs(i, connect1, 0))

print(result)
'''



# 1967 :









##

# 11047 동전 0

n, k = map(int,input().split())

A = []
for i in range(n) :
    A. append(int(input()))

cnt = 0
while k != 0 :
    for j in range(n-1,-1,-1) :
        if A[j] <= k :
            k -= A[j]
            print(A[j], k)
            cnt +=1
            break
print(cnt)