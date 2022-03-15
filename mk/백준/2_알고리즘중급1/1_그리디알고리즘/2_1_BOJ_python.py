# 11047 - 동전 0

N, K = map(int, input().split())
values = []

for i in range(N):
    values.append(int(input()))

values.reverse()
count = 0

for i in values:
    count += K // i
    K -= (K//i) * i

print(count)


# 1931 - 회의실 배정

N = int(input())
reserve = []
for i in range(N):
    reserve.append(list(map(int, input().split())))

reserve = sorted(reserve, key=lambda a : (a[1], a[0]))
reserved = [[0, 0]]
count = 0

for i in reserve:
    if reserved[-1][1] <= i[0]:
        reserved.append(i)
        count += 1

print(count)



