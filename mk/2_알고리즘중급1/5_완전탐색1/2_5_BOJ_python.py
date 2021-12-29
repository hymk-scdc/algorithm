# 1697 - 숨바꼭질
'''
반례
TEST CASE #3:
15964 89498
exp -> 4781
you -> 19110

3 43
출력: 7
정답: 6
3 -> 6 -> 12 -> 11 -> 22 -> 44 -> 43

4 27
출력: 6
정답: 5
4 -> 8 -> 7 -> 14 -> 28 -> 27

5 35
출력: 6
정답: 5
5 -> 10 -> 9 -> 18 -> 36 -> 35

6 43
출력: 6
정답: 5
6 -> 12 -> 11 -> 22 -> 44 -> 43

7 43
출력: 7
정답: 6
7 -> 6 -> 12 -> 11 -> 22 -> 44 -> 4
'''
import math

N, K = map(int, input().split())
cnt = 0
while (N!=K):
    if (abs(N-K) < (1+N)/2):
        if K < N:
            N -= 1
        else:
            N += 1
        cnt += 1
        print(cnt, "+1칸,", N)
    elif (abs(2*N-K)//2 < (1+N)/2):
        add1 = math.trunc((K-2*N)/2)
        N += math.trunc((K-2*N)/2)
        cnt += abs(add1)
        print(cnt, add1, "칸 이동, ", N)
        N *= 2
        cnt += 1
        print(cnt, "2배, ", N)
    else:
        N = 2*N
        cnt += 1
        print(cnt, "2배, ", N)
print('결과', cnt)

# 제출용
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

print(cnt)