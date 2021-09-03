## 개미 전사
N = int(input()) # 식량창고의 개수

food = list(map(int,input().split()))# 식량창고에 들어있는 식량 양

def ANT(n, food) :
    dp = [0] * n
    for i in range(n) :
        if i < 2 :
            dp[i] = food[i]
        else :
            dp[i] = dp[i-2] + food[i] # dp[i] = max(dp[i-1], dp[i-2]+food[i])
    return max(dp) # dp[n-1]

print(ANT(N,food))


## 효율적인 화폐구성

N, M = map(int, input().split())
ns = [] # 화폐종류
dp = [0]*(M+1) # 답 dp[i]는 금액 i를 만들 수 있는 최소한의 화폐 개수

# 화폐종류 넣어놓기
for _ in range(N) :
    n = int(input())
    ns.append(n)

# 답 채우기
for i in range(0,M+1) : # 구해야 하는 값까지 반복
    if i < min(ns) : # 화폐종류 중 가장 작은 거보다 작으면 -1
        dp[i] = -1
    elif i in ns : # 화폐종류와 같으면 1
        dp[i] = 1
    else :
        for j in ns : # i에서 화폐종류 별로 뺀 값의 답 중 가장 작은 것 + 1이 dp[i]
            temp = []
            if (i-j) >= min(ns) :
                temp.append(i-j)
                temp2 = []
                for k in temp :
                    temp2.append(dp[k])
                    dp[i] = min(temp2) + 1
            else :
                dp[i] = -1

print(dp[M])


### 강사님 코드
n, m = map(int, input().split())

array = []

for i in range(n) :
    array.append(int(input()))

d = [10001] *(m+1)

d[0] = 0
for i in range(n) :
    for j in range(array[i], m+1) :
        if d[j-array[i]] != 10001 :
            d[j] = min(d[j], d[j-array[i]] + 1)
if d[m] == 10001 :
    print(-1)
else : print(d[m])


## 금광문제

T = int(input())

for _ in range(T) :
    n, m = map(int, input().split())

    golds = list(map(int, input().split()))
    matrix = []
    for _ in range(n) :
        matrix.append(list(golds[:m]))
        golds = golds[m:]


    dp = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(m) :
        for i in range(n) :
            if i == 0 : # 제일 위의 행일 때
                dp[i][j] = matrix[i][j] + max(dp[0][j-1], dp[1][j-1])
            elif i == n-1 : # 제일 아래 행일 때
                dp[i][j] = matrix[i][j] + max(dp[n-2][j-1], dp[n-1][j-1])
            else :
                dp[i][j] = matrix[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

    result = max(list(dp[i][m-1] for i in range(n)))

    print(result)


## 병사 배치하기 :  O(N^2) 이하의 프로그래밍

