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