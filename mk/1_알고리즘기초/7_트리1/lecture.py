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
        pre_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None:
        pre_order(tree[node.right_node])


# 후위 순회
def post_order(node):
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])
    print(node.data, end='')


n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])



#


from collections import deque
import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n) :
    temp = list(map(int, sys.stdin.readline().split()))
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
        head, node, link  = temp[0], temp[1], temp[2] # 연결된 앞, 뒤, 길이
        if visited[node] == -1 :
            visited[node] = visited[head] + link
            for tu in tree[node] : # node에 연결된 애들 다 append
                queue.append(tu)

    return visited.index(max(visited)) # 최대인 애로 다시 돌게..그러면 최대인 애에서 또 최대인 애가 나오겠지

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