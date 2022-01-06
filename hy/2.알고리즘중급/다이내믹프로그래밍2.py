# 동전2

n , k = map(int,input().split())

coins = []

for _ in range(n) :
    coins.append(int(input()))

coins.sort(reverse=True)

def coincnt(coins,k, start) :
    cnt = 0
    s, r = 0, None
    while (r != 0) and (start != n) :
        coin = coins[start]
        s = k//coin # 몫
        r = k%coin # 나머지
        k = r # 남은 값어치
        cnt += s
        start += 1
    if r != 0 :
        cnt = -1
    return cnt


result = 10001
for i in range(n) :
    count = coincnt(coins,k,i)
    if count != -1 :
        result = min(result, count)


if result == 10001 :
    print(-1)
else :
    print(result)

#
# n , k = map(int,input().split())
#
# coins = []
#
# for i in range(n) :
#     coins.append(int(input()))
#
# coins.sort(reverse=True)
#
#
# def coincnt(coins,k, start) :
#     cnt = 0
#     s, r = 0, None
#     try :
#         while r != 0 or start != n :
#                 coin = coins[start]
#                 s = k//coin # 몫
#                 r = k%coin # 나머지
#                 k = r # 남은 값어치
#                 cnt += s
#                 start += 1
#     except :
#         cnt = -1
#     return cnt
#
#
#
# result = 10001
# for i in range(n) :
#     count = coincnt(coins,k,i)
#     if count != -1 :
#         result = min(result, count)
#
#
# if result == 10001 :
#     print(-1)
# else :
#     print(result)






# 내리막 길