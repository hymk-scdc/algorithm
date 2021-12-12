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




