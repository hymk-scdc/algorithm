# 2021.08.25

# 1463 : 1로 만들기
'''
연산
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.


3 : 1 - 1번
4 : 2,2 - 2번
5 : 3,2,2, - 3번
6 : 1,2 - 2번
7 : 3,1,2 - 3번
8: 2,2,2 - 3번
9 : 1,1 - 2번
10 : 2,3,2,2, - 4번
     3,1,1 - 3번
11 : 3, func(10) - 4번
12 : 3, func(11) - 4
     2, func(6) - 3
     1, func(4) - 3
13 : 3, func(12) - 4
14 : 2, func(7) - 4
     3, func(13) - 5

경우 1 : 2,3으로 안 나눠떨어짐 - 3번 연산
경우 2 : 2로 나눠떨어짐 - 3번 연산하거나 2번 연산
경우 3 : 3으로 나눠떨어짐 - 3번 연산하거나 1번 연산
경우 4 : 2,3으로 나눠떨어짐 -

대충 최소인 숫자 호출하기,,?

# 탑다운
import sys
sys.setrecursionlimit(10**7)

X = int(sys.stdin.readline())
def func(num):
    if num == 1:
        return 0
    elif num % 2 and num % 3 == 0:
        return min(func(num / 2), func(num / 3), func(num-1)) + 1
    elif num % 2 == 0:
        return min(func(num / 2), func(num - 1)) + 1
    elif num % 3 == 0:
        return min(func(num / 3), func(num - 1)) + 1
    else:
        return func(num-1) + 1

result= func(X)
print(result)

'''
# 보텀업

import sys

X = int(sys.stdin.readline())
memo = [0] * (1000000+1)

for num in range(2, X+1):
    if num % 2 == 0 and num % 3 == 0:
        memo[num] = min(memo[num//2], memo[num//3], memo[num-1]) + 1
    elif num % 2 == 0:
        memo[num] = min(memo[num//2], memo[num-1]) + 1
    elif num % 3 == 0:
        memo[num] = min(memo[num//3], memo[num-1]) + 1
    else:
        memo[num] = memo[num-1] + 1

print(memo[X])


# 11726 : 2xn 타일링

'''
피보나치 수열

# 탑다운 방식 - 시간 초과,, 메모이제이션 사용해도 시간 초과
import sys
N = int(sys.stdin.readline())
d = [0]*(N+1)

def result(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if d[num] != 0:
        return d[num]
    return result(num-1) + result(num-2)

print(result(N) % 10007)
'''

# 보텀업

import sys
N = int(sys.stdin.readline())

DP = [1, 2] + [0]*1000

for i in range(2, N+1):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[N-1] % 10007)


# 11727 : 2×n 타일링 2

import sys
N = int(sys.stdin.readline())

DP = [1, 3] + [0]*1000

for i in range(2, N+1):
    DP[i] = DP[i-1] + 2 * DP[i-2]

print(DP[N-1] % 10007)


# 9095 : 1,2,3 더하기

import sys
N = int(sys.stdin.readline())

DP = [1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2, N+1):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

print(DP[N-1])
