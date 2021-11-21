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
'''
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
다시 해서 해결
def 문 안의 if문 부분 좀 바꿈
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
    for child in childs[parent]:  # child : 4, 6 / parent : 1
        if parents[child] == 0:
            parents[child] = parent
            parent_pop(child)
    return


parent_pop(1)
for i in parents[2:]:
    print(i)
