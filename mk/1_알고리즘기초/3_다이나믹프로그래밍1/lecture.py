# DP 강의 : https://www.youtube.com/watch?v=5Lu34WIx2Us

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
