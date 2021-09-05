# DP 강의

# [(이코테 2021 강의 몰아보기) 6. 다이나믹 프로그래밍](https://www.youtube.com/watch?v=5Lu34WIx2Us)


# 문제 : 개미 전사
'''
입력 :
N (개수)
공백을 기준으로 각 식량의 개수 K
조건 : 인접한 식량은 빼앗을 수 없음
출력 : 최댓값
'''

import sys

N = int(sys.stdin.readline())
P = list(map(int, input().split(" ")))
DP = [0] * 100  # 그놈까지의 최댓값
DP[0] = P[0]
DP[1] = max(P[0], P[1])
#DP[2] = max(DP[0] + P[2], DP[1])
#DP[3] = max(DP[1] + P[3], DP[2])

for i in range(2, N):
    DP[i] = max(DP[i-2] + P[i], DP[i-1])

print(DP[N-1])



# 효율적인 화폐 구성
'''
해설 코드와 다름
아래 해설 코드

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
'''

N, M = map(int, input("").split(" "))
P = []
for i in range(N):
    P.append(input(""))

dp = [0] + [10001] * (M)  # [0, -1이 M개]... dp[i]는 i원을 만드는 최소 개수. 중첩 for 문으로 dp[i]를 계속 업데이트

for j in range(1, M+1):
    for i in P:
        if dp[j % int(i)] != -1:
            dp[j] = min( j//int(i) + dp[j % int(i)], dp[j] )
        else:
            continue

if dp[-1] != 10001:
    print(dp[-1])
else:
    print(-1)


# 금광
T = int(input())
for i in range(T):
    n, m = map(int, input("").split(" "))
    num = list(map(int, input().split(" ")))

    array = [[0 for i in range(n+2)]]

    dp = []  # 앞놈 중에 최댓값 더한 놈 (해당 인덱스 열까지의 최댓값이 저장,, 모든 행 값이 다 있음)
    for i in range(m + 1):
        dp.append([0 for i in range(n + 2)])

    for i in range(0, m):
        array.append([0] + [num[j] for j in range(i, n*m, m)] + [0])

    for i in range(1, m+1):
        for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + array[i][j]

    print(max(dp[-1]))


# 병사 배치하기
'''
전투력이 최대가 되게 한거다

N = int(input(""))
P = list(map(int, input().split(" ")))

dp = [P[0], 0]

cnt = 0

for i in P[1:]:
    if dp[0] - dp[1] < i:
        if dp[0] < i:  # 바꿔야하는 경우임
            dp = [i, 0]
            cnt += 1
        else:  # 안 바꾸는 경우
            continue

    elif dp[-2] - dp[-1] > i:
        for j in range(len(dp)):
            dp[j] = dp[j] + i
        dp.append(0)

    else:
        for j in range(len(dp) - 2):
            if dp[j] - dp[j+1] > i > dp[j+1] - dp[j+2]:
                if dp[j+1] < i: # 바꿔야 함
                    for k in range(j+1):
                        dp[k] = dp[k] - dp[j+1] + i
                    dp = dp[:j+1] + [i, 0]
                    cnt += 1
                else:
                    continue
print(cnt)
'''
# 틀린 내 풀이

N = int(input(""))
P = list(map(int, input().split(" ")))

dp = [10000001, P[0]]

cnt = 0

for i in range(1, N):
    if dp[-2] > P[i] > dp[-1]:  # 바꿔
        dp[-1] = P[i]
        cnt += 1
    elif dp[-2] < P[i]:  # pass
        continue
    else:  #dp[-1] > P[i]
        dp.append(P[i])

print(cnt)


'''
결국 못 풀고 해설 들음
해설)
가장 긴 증가하는 부분 수열 (LIS) 알고리즘
D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
D[i] = max(D[i], D[j]+1) if array[j] < array[i]
'''

# 푸는 로직 듣고 작성한 코드

N = int(input(""))
P = list(map(int, input().split(" ")))

dp = [1] * 2000

P.reverse()

for i in range(1, N):
    for j in range(i):
        if P[j] < P[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(len(P)-max(dp))





