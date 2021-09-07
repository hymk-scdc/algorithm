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
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())

    DP = [1, 2, 4, 0, 0, 0, 0, 0, 0, 0]

    for i in range(3, N):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

    print(DP[N-1])


# 11052 : 카드 구매하기
'''
0829 와앙 모르겠는데
0830 와 진짜 모르겠는뎅

0905)
내 풀이 != 학영언니 풀이 = 모범답안 풀이
그래도 내 풀이도 맞는 것 같고 시간복잡도 더 낮은듯??

내 풀이는 n^2/2 ?? 모범답안 n^2.. n^2/2도 n^2인 것 같긴 한데
'''

import sys
N = int(sys.stdin.readline())
P = sys.stdin.readline().rstrip().split(" ")
d = list(map(int, P))

for i in range(1, N):
    for j in range((i+1)//2):
        #print("max(d{}, d[{}]+d[{}])".format(i, j, i-j-1), d[i], d[j], "+", d[i-j-1])
        d[i] = max(int(d[i]), d[j]+d[i-j-1])
        #print("P", P)
        #print("d", d)


print(d[-1])


# 학영
n = int(input())
p = [0] + list(map(int, input().split()))
dp =[0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i+1):
        print("max(dp{}, dp[{}]+p[{}])".format(i, i-j, j), dp[i], dp[i-j],"+", p[j])
        print("p", p)
        print("d", dp)
        dp[i] = max(dp[i], dp[i-j] + p[j])
print(dp[n])

# 10844 : 쉬운 계단 수
'''
1. 이전 경우의 수에서 바로 연산할 수 있는지 해봤는데 잘 모르겠음
2. 이전 경우의 수를 전부 탐색

0905) 아예 방향 틀어서 풀었음! 
'''

import sys
N = int(sys.stdin.readline())

d = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

for i in range(1, N):
    d_new = [0]
    for j in range(1, 11):
        d_new.append(d[j-1] + d[j+1])
    d_new.append(0)
    d = d_new

print(sum(d) % 1000000000)


# 11057 : 오르막 수
N = int(input(""))
DP = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    for j in range(10):
        DP[j + 1] = DP[j] + DP[j + 1]

print(sum(DP) % 10007)


# 2193 : 이친수
N = int(input(""))

DP = [0, 1]

for i in range(1, N):
    DP = [DP[0] + DP[1], DP[0]]

print(sum(DP))

