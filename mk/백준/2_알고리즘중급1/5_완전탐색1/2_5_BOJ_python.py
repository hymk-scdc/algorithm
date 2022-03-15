# 1697 - 숨바꼭질

'''
나 : 그때그때 최적의 해
답안 : bfs로 경우의 수 - 가장 먼저 도달한 놈

반례
TEST CASE #3:
15964 89498
exp -> 4781
you -> 19110

3 43
출력: 7
정답: 6
3 -> 6 -> 12 -> 11 -> 22 -> 44 -> 43

5 35
출력: 6
정답: 5
5 -> 10 -> 9 -> 18 -> 36 -> 35

6 43
출력: 6
정답: 5
6 -> 12 -> 11 -> 22 -> 44 -> 43

4 27
출력: 6
정답: 5
4 -> 8 -> 7 -> 14 -> 28 -> 27

7 43
출력: 7
정답: 6
7 -> 6 -> 12 -> 11 -> 22 -> 44 -> 4

'''

# 검색 답안
from collections import deque
def bfs():
    q = deque()
    q.append(N)
    cnt = 0
    while q:
        print(cnt,'회',q)
        v = q.popleft()
        if v == K:
            print(time[v])
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[v] + 1
                q.append(next_step)
        cnt+=1

MAX = 100001
N, K = map(int, input().split())
time = [0]*MAX
bfs()


## 내꺼 - 반례 틀림
import math

N, K = map(int, input().split())
cnt = 0
while (N != K):
    if (abs(N - K) < (1 + N) / 2):
        if K < N:
            N -= 1
        else:
            N += 1
        cnt += 1
        print(cnt, "+1칸,", N)
    elif (abs(2 * N - K) // 2 < (1 + N) / 2):
        add1 = math.trunc((K - 2 * N) / 2)
        N += math.trunc((K - 2 * N) / 2)
        cnt += abs(add1)
        print(cnt, add1, "칸 이동, ", N)
        N *= 2
        cnt += 1
        print(cnt, "2배, ", N)
    else:
        N = 2 * N
        cnt += 1
        print(cnt, "2배, ", N)
print('결과', cnt)

## 내꺼 일반화 - 반례 틀림
import math

N, K = map(int, input().split())
cnt = 0
while (N != K):
    a = round(K / N)
    if abs(a * N - K) // a < (1 + N) / 2:
        add1 = math.trunc((K - a * N) / a)
        N += math.trunc((K - a * N) / a)
        cnt += abs(add1)
        print(cnt, add1, "칸 이동, ", N)
        if a >= 2:
            N *= 2
            cnt += 1
            print(cnt, a, "배, ", N)
        else:
            continue
    else:
        N = 2 * N
        cnt += 1
        print(cnt, "2배, ", N)
print('결과', cnt)

#

'''
# 내꺼 제출용
import math

N, K = map(int, input().split())
cnt = 1
while (N!=K):
    if (abs(N-K) < (1+N)/2):
        if K < N:
            N -= 1
        else:
            N += 1
        cnt += 1
    elif (abs(2*N-K)//2 < (1+N)/2):
        add1 = math.trunc((K-2*N)/2)
        N += add1
        cnt += add1
        N *= 2
        cnt += 1
    else:
        N = 2*N
        cnt += 1

print(cnt)'''


# 1987 알파벳
'''
검색 답안 : 방문한 알파벳 중복 없이 넣는 visited 를 set로 함 - 맞음
원래 내꺼 : 방문한 알파벳 중복 없이 넣는 visited 를 리스트로 함 - 시간 초과

왜 시간초과 차이가 나는지 모르겠음....
'''
R, C = map(int, input().split())
words = []
for i in range(R):
    words.append(list(input()))

visited = set(words[0][0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
maxnum = 0

def dfs(x, y, cnt):
    global maxnum
    maxnum = max(maxnum, cnt)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if (0<=nx<=R-1 and 0<=ny<=C-1 and words[nx][ny] not in visited):
            print(visited)
            visited.add(words[nx][ny])
            #print(word)
            dfs(nx, ny, cnt+1)
            visited.remove(words[nx][ny])


dfs(0, 0, 1)
print(maxnum)


# 원래 내꺼 : 방문한 알파벳 중복 없이 넣는 visited 를 리스트로 함
R, C = map(int, input().split())
words = []
for i in range(R):
    words.append(list(input()))

visited = [words[0][0]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
maxnum = 0

def dfs(x, y, cnt):
    global maxnum
    maxnum = max(maxnum, cnt)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if (0<=nx<=R-1 and 0<=ny<=C-1 and words[nx][ny] not in visited):
            visited.append(words[nx][ny])
            #print(word)
            dfs(nx, ny, cnt+1)
            visited.pop()


dfs(0, 0, 1)
print(maxnum)


# 학영 집합
n, m = map(int,input().split())

class Node() :
    def __init__(self, parent):
        self.parent = parent
num = []
for i in range(n+1) :
    num.append(Node(i))


def setroot(a,b) : # union
    ap = findroot(a)
    bp = findroot(b)
    if ap <= bp :
        num[bp].parent = num[ap].parent
    else :
        num[ap].parent = num[bp].parent


def findroot(a) : # find
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