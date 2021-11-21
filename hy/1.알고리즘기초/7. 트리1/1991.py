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






