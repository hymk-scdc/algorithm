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
n = int(input())
# s = []
# e = []
t = []
for i in range(n) :
    # st, et = map(int,input().split())
    # s.append(st)
    # e.append(et)

    t.append(list(map(int,input().split())))

cnt = 0
start = 0
end = 2**31-1
# while start <= max(s) :
#     for i in range(n) :
#         if s[i] >= start :
#             end = min(e[i], end)
#     cnt += 1
#     start = end
#     end = 2**31-1
#
# print(cnt)


n = int(input())
t = []
for i in range(n) :
    t.append(list(map(int, input().split())))


t.sort()

end = 2**31-1
cnt = 1

for i in range(n) :
    if t[i][0] >= end :
        cnt +=1
        end = t[i][1]
    else :
        end = min(end, t[i][1])

print(cnt)


# 10816 숫자카드2
n = int(input())
card = list(map(int,input().split()))
m = int(input())
cardNum = list(map(int,input().split()))
cntP = [0] * 10000001
cntN = [0] * 10000001

for i in card :
    if i <0 :
        cntN[i] +=1
    else :
        cntP[i] +=1

for j in cardNum :
    if j < 0 :
        print(cntN[j], end = ' ')
    else :
        print(cntP[j], end = ' ')

# '''분할정복으로 풀어보기'''
# card.sort()
# mid = int(n//2)
#
# left = card[mid]
# right = card[mid+1]
#
# if left >= card[mid]


# 11729 하노이 탑 이동 순서
n = int(input())
def hanoi(n,a,b,c) :
    if n == 1 :
        print(a,c)
    else :
        hanoi(n-1, a, c, b)
        print(a,c)
        hanoi(n-1, b, a, c)

cnt = 1
if n == 1 :
    cnt = 1
else :
    for i in range(n-1) :
        cnt = cnt*2 + 1

print(cnt)
hanoi(n,1,2,3)

# 2261 가장 가까운 두 점

n = int(input())
dot = []
distance = 800000000

for i in range(n) :
    x, y = map(int,input().split())
    dot.append((x,y))

for i in range(n) :
    x, y = dot[i]
    for j in range(i+1,n) :
        cx, cy = dot[j]
        distance = min(distance , (x-cx)**2 + (y-cy)**2)

print(distance)

# 분할정복
n = int(input())
dot = []

for i in range(n) :
    x, y = map(int,input().split())
    dot.append([x,y])


dot.sort()

def dist(dot1, dot2) :
    return (dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2

def min_dist(dot, n) :
    if n == 2 :
        return dist(dot[0], dot[1])
    elif n == 3 :

        return min(dist(dot[0], dot[1]), dist(dot[1], dot[2]), dist(dot[0], dot[2]))
    else :
        mid = n//2

        left = min_dist(dot[:mid], mid)
        right = min_dist(dot[mid:], n-mid)


        mid_dist = min(left, right)

        temp= []

        for i in range(n) :
            if (dot[i][0] - dot[mid][0])**2 < mid_dist :
                temp.append(dot[i])


        if len(temp) >= 2 :
            temp.sort(key = lambda y : y[1])

            for i in range(len(temp)-1) :
                for j in range(i+1,len(temp)) :
                    if (temp[i][1] - temp[j][1])**2 > mid_dist :
                        break
                    temp_dist = dist(temp[i], temp[j])
                    # print(f'before : {mid_dist}')
                    mid_dist = min(mid_dist, temp_dist)
                    # print(f'after : {mid_dist}')

        return mid_dist

print(min_dist(dot,n))




# 1654 랜선자르기

K, N = map(int,input().split())

line = []

for _ in range(K) :
    line.append(int(input()))


start = 1
end = max(line)


while start <= end :
    mid = (start + end)//2

    cnt = 0
    for i in line :
        cnt += i // mid

    if cnt >= N :
        start = mid + 1
    else :
        end = mid - 1

print(end)

# 2805 나무자르기

N, M = map(int, input().split())

tree = list(map(int, input().split()))

start = 0
end = max(tree)

while start <= end :
    mid = (start + end) // 2

    total = 0
    for i in tree :
        if i - mid >= 0 :
            total += i-mid
    if total >= M :
        start = mid + 1
    else :
        end = mid -1

print(end)


# 11723 집합
import sys
n = int(sys.stdin.readline())
s = set()

for _ in range(n) :
    order = sys.stdin.readline().split()
    if len(order) == 1 :
        if order[0] == 'all':
            # s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
            s = {i for i in range(1,21)}
        else:
            s = set()
    else :
        command, num = order[0], int(order[1])
        if command == 'add' :
            s.add(num)
        elif command == 'remove' :
            s.discard(num)
        elif command == 'toggle' :
            if num in s :
                s.discard(num)
            else :
                s.add(num)
        elif command == 'check' :
            print(1 if num in s else 0)

# 10972 다음 순열

import sys
n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

cnt = 0
for i in range(1,n) :
    if num[i] <= num[i-1] :
        cnt +=1

if cnt == (n-1) :
    print(-1)
else :
    print()
