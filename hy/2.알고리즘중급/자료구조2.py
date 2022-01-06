# 1717 집합의 표현
'''
자료구조 중 노드 구조로 확인
집합의 대표값 하나인 부모 노드끼리만 비교하여 진행
(화요일에 이거 다시 코드 짜보기)
'''
n, m = map(int, input().split())
li = []
for _ in range(m) :
   o, a, b = map(int, input().split())
   if o == 0 :
       a_idx = '없음'
       b_idx = '없음'
       for j in range(len(li)):
           if a in li[j] :
               a_idx = j
           if b in li[j] :
                b_idx = j
       if b_idx == '없음' and a_idx != '없음' :
           li[a_idx] = li[a_idx].union({b})
       elif a_idx == '없음' and b_idx == '없음' :
           li.append({a,b})
       elif a_idx == '없음' and b_idx != '없음' :
           li[b_idx] = li[b_idx].union({a})
       else :
           if a_idx != b_idx:
               set_a, set_b = li[a_idx], li[b_idx]
               li.remove(set_a)
               li.remove(set_b)
               li.append(set_a.union(set_b))
   else :
       ans = 'NO'
       for j in range(len(li)):
           if a in li[j] and b in li[j] :
               ans = 'YES'
               break

       print(ans)

n, m = map(int,input().split())

class Node() :
    def __init__(self, parent):
        self.parent = parent

num = []
for i in range(n+1) :
    num.append(Node(i))

# def setroot(a,b) :
#     if num[b].parent == b :
#         num[b].parent = a
#         return
#     else :
#         if a <= num[b].parent :
#             setroot(a,num[b].parent)
#         else :
#             setroot(num[b].parent, a)

def setroot(a,b) :
    ap = findroot(a)
    bp = findroot(b)
    if ap <= bp :
        num[bp].parent = num[ap].parent
    else :
        num[ap].parent = num[bp].parent

# def findroot(a) :
#     global root
#     if num[a].parent == a :
#         root = a
#         return root
#     else :
#         findroot(num[a].parent)
#     return root

def findroot(a) :
    while num[a].parent != a :
        p = num[a].parent
        num[a].parent = num[p].parent
        a = p
    return num[a].parent

for j in range(m) :
    o , a , b = map(int, input().split())
    if o == 0 :
        if a < b :
            setroot(a,b)
        else :
            setroot(b,a)
    else :
        if findroot(a) == findroot(b) :
            print('YES')
        else :
            print('NO')


# 2606 바이러스

n = int(input())
m = int(input())

com = []
for i in range(n+1) :
    com.append([i])

for i in range(m) :
    a, b = map(int,input().split())
    com[a].append(b)
    com[b].append(a)

visited = [0] * (n+1)

from collections import deque

def bfs(a) :
    queue = deque()
    queue.append(a)
    visited[a] = 1
    cnt = 0
    while queue :
        # print(queue)
        # print(visited)
        num = queue.popleft()
        # print('-----', num)
        cnt += 1
        # print('cnt : ', cnt)
        for i in com[num] :
            if visited[i] == 0 :
                # print('i : ', i)
                visited[i] = 1
                queue.append(i)
    return cnt-1

print(bfs(1))
