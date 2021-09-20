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


# 9465 : 스티커
'''
너어는 진짜.. 며칠 붙잡고 있었음
'''
# 내꺼 : 답 맞게 나오는거 같은데 틀렸대.. 코드도 길기는 해서 다시 해볼까봐

T = int(input(""))
for i in range(T):
    N = int(input(""))
    point = []  # point[0]은 1행, point[1]은 2행
    point.append(list(map(int, input().split(" "))))
    point.append(list(map(int, input().split(" "))))

    # 초항 넣기
    if point[0][0] < point[1][0]:
        DP = [point[1][0]]
        last = [1, 0]  # [마지막놈의 행, 아닌거]
    else:
        DP = [point[0][0]]
        last = [0, 1]

    # 2항 넣기
    if point[0][0]+point[1][1] > point[1][0]+point[0][1]:
        DP.append(point[0][0]+point[1][1])
        last = last + [1, 0]  # [전열(dp[i-2]): 마지막놈의 행, 아닌거 / 마지막열dp[i-1]: 마지막놈의 행, 아닌거]
    else:
        DP.append(point[1][0]+point[0][1])
        last = last + [0, 1]

    for i in range(2, N):
        # 3가지 비교
        # DP[i-2] + point[n_last][i-1] + point[last][i]    DP[i-2] + point[n_last][i]     DP[i-1] + point[n_last][i]
        if DP[i-2]+point[last[1]][i-1]+point[last[0]][i] > max(DP[i-2]+point[last[1]][i], DP[i-1]+point[last[3]][i]):
            DP.append(DP[i-2]+point[last[1]][i-1]+point[last[0]][i])
            print("1", DP, point[last[1]][i-1]+point[last[0]][i], i)
            last = last[2:] + last[:2]
        elif DP[i-2] + point[last[1]][i] > max(DP[i-2]+point[last[1]][i-1]+point[last[0]][i], DP[i-1]+point[last[3]][i]):
            DP.append(DP[i-2] + point[last[1]][i])
            print("2", DP,  point[last[1]][i], i)
            last = last[2:] + last[:2][::-1]
        else:
            DP.append(DP[i-1]+point[last[3]][i])
            print("3", DP, point[last[3]][i], i)
            last = last[2:] + last[2:][::-1]
    print(DP[-1])


# 내가 다시 한 거
'''
해설 봄 : 앞놈이 건너뛴 놈으로 선택됐을 때는 dp[i-2] + array[i-1]이랑 dp[i-1]이랑 달라져서 틀린 거였음 
위 코드 반례 : 10 1 1 20 / 5 1 100 1

'''
T = int(input(""))
for i in range(T):
    N = int(input(""))
    point = []
    point.append([0, 0]+list(map(int, input().split(" "))))
    point.append([0, 0]+list(map(int, input().split(" "))))
    dp = [[point[0][0], point[1][0]+point[0][1]] + [0]*(N)
        , [point[1][0], point[1][1]+point[0][0]] + [0]*(N)]

    for i in range(2, N+2):
        dp[0][i] = max(dp[1][i-1]+point[0][i], dp[1][i-2]+point[0][i])
        dp[1][i] = max(dp[0][i-1]+point[1][i], dp[0][i-2]+point[1][i])

    print(max(dp[0][-1], dp[1][-1]))



# 2156 : 포도주 시식
'''
하.....너무 힘들었다.... 너무 오래 걸렸다.. 한 이틀?걸렸나 4시간은 쓴듯
'''
n = int(input(""))
drink = [0]

for i in range(n):
    drink.append(int(input("")))

if len(drink) == 2:
    print(drink[1])
elif len(drink) == 3:
    print(drink[1]+drink[2])
else:
    dp = [0, drink[1], drink[1]+drink[2]]
    cnt = 2
    for i in range(3, len(drink)):
        dp.append(max(dp[i-3]+drink[i-1]+drink[i], dp[i-2]+drink[i], dp[i-1]))

    print(dp[-1])


# 11053 : 가장 긴 증가하는 부분 수열
N = int(input(""))
A = list(map(int, input().split()))
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# 11055 : 가장 큰 증가 부분 수열
N = int(input(""))
A = list(map(int, input().split()))
dp = A[:]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+A[i])

print(max(dp))


# 11722 : 가장 긴 감소하는 부분 수열
N = int(input(""))
A = list(map(int, input().split()))
A.reverse()
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# 11054 : 가장 긴 바이토닉 부분 수열
N = int(input(""))
A = list(map(int, input().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

A.reverse()
dp2 = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp2[i] = max(dp2[i], dp2[j]+1)
dp2.reverse()

result = []
for i in range(N):
    result.append(dp[i]+dp2[i]-1)

print(max(result))


# 1912 : 연속합
'''
시간 초과

N = int(input(""))
A = list(map(int, input().split()))
dp = []
for i in range(N):
    result = []
    for j in range(i+1):
        result.append(sum(A[j:i+1]))
    dp.append(max(result))
print(max(dp))

'''

N = int(input(""))
A = list(map(int, input().split()))
dp = [A[0]]
for i in range(1, N):
    if dp[i-1] + A[i] < A[i]:
        dp.append(A[i])
    else:
        dp.append(dp[i-1]+A[i])

print(max(dp))


# 2579 : 계단 오르기
'''
max(dp[-3]+A[i-1]+A[i], dp[-2]+A[i], dp[-1] 가 아닌 이유는 x가 연속 두 번이면 안돼서
'''
n = int(input(""))
A = []
for i in range(n):
    A.append(int(input("")))
if n < 3:
    print(sum(A))
else:
    dp = [A[0], A[0]+A[1], A[2]+max(A[0], A[1])]
    for i in range(3, n):
        dp.append(max(dp[-3]+A[i-1]+A[i], dp[-2]+A[i]))
    print(dp[-1])


# 1699 : 제곱수의 합
'''
반례 : 12 = 4+4+4 / 9+1+1+1

N = int(input(""))
dp = [0] * 100000

for i in range(1, N+1):
    if i**0.5 % 1 == 0:
        dp[i] = 1
    else:
        dp[i] = dp[int(i**0.5)**2] + dp[i-int(i**0.5)**2]
print(dp[N])
'''

N = int(input(""))
dp = [0] * 100000

for i in range(1, N+1):
    if i**0.5 % 1 == 0:
        dp[i] = 1
    else:
        result = []
        for j in range(1, int(i**0.5)+1):
                result.append(dp[j**2] + dp[i - j**2])
        dp[i] = min(result)
print(dp[N])


# 2133 : 타일 채우기

N = int(input(""))
if N % 2 != 0:
    print(0)
else:
    N = int(N/2)
    dp = [1, 3, 11, 41]
    if N < 4:
        print(dp[N])
    else:
        for i in range(4, N+1):
            dp.append(2*sum(dp)+dp[-1])
        print(dp[N])


# 9461 : 파도반 수열

T = int(input(""))
dp = [0, 1, 1, 1, 2, 2]
for t in range(T):
    N = int(input(""))
    for i in range(len(dp), N+1):
        dp.append(dp[i-1]+dp[-5])
    print(dp[N])


# 2225 : 합분해
'''
0도 포함인 걸 빼먹었었음
'''
N, K = list(map(int, input("").split(" ")))

dp = [[1 for i in range(0, 201)], [i for i in range(0, 201)]]
for i in range(200):
    dp.append([1]*201)

for i in range(2, N+1):
    for j in range(2, K+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[N][K] % 1000000000)


# 2011 : 암호코드

N = list(map(int, input("")))
N.reverse()
dp = [1, 1]
num1 = N.pop()

if num1 == 0:
    print(0)
    exit()

for i in range(2, len(N)+2):
    num2 = N.pop()

    if (num1 == 1 and num2 != 0) or (num1 == 2 and 0 < num2 < 7):
        dp.append(dp[i-1]+dp[i-2])
    elif (num1 == 0 and num2 != 0) or (2 < num1 <= 9 and num2 != 0) \
            or (num1 == 2 and 6 < num2 <= 9):
        dp.append(dp[i-1])
    elif 0 < num1 < 3 and num2 == 0:
        dp.append(dp[i-2])
    else:
        dp.append(0)
        break
    num1 = num2

print(dp[-1] % 1000000)


# 다른 풀이 도전
