# 11047 동전 0

n, k = map(int,input().split())

A = []
for i in range(n) :
    A. append(int(input()))

cnt = 0
while k != 0 :
    for j in range(n-1,-1,-1) :
        if A[j] <= k :
            k -= A[j]
            cnt +=1
            break
print(cnt)


# 1931번 회의실 배정