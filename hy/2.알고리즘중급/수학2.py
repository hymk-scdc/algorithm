# 1629 곱셉
'''반례 짱 많음 10,5,12  5,6,11'''
a,b,c = map(int,input().split())

result = []
start = 0
if b == 1 :
    print(a%c)
else :
    temp = 1
    for i in range(b) :
        temp = temp * a

        if temp < c :
            result.append(temp)
        else :
            r = temp%c
            if r not in result :
                result.append(r)
            else :
                if result[start] == r :
                    break
                else :
                    result.append(r)

    if i == b-1 :
        print(r)
    else :
        print(result[b%i-1])

'''패턴 찾을 때까지 반복하기 '''
import sys
a,b,c = map(int,sys.stdin.readline().split())

result = []
temp = 1

if b == 1 :
    print(a%c)
else :
    for i in range(b) :
        temp = temp * a
        r = temp%c
        result.append(r)
        if r in result :
            break

    if i == b-1 :
        print(r)
    else :
        print(result[b%i-1])
print(f'길이 : {len(result)-1}')

import sys
a,b,c = map(int,sys.stdin.readline().split())

def gob(a,n) :
    if n == 1 :
        return a%c
    else :
        tmp = gob(a,n//2)
        if n % 2 == 0 :
            return (tmp*tmp)%c
        else :
            return (tmp*tmp*a)%c

print(gob(a,b))



# 피보나치 수 2

n = int(input())

dp = [0,1]

for i in range(2,n+1) :
    dp.append(dp[i-1]+dp[i-2])

print(dp[n])


# 1016 제곱 ㄴㄴ 수

mi, ma = map(int,input().split())

ma_root = int(ma**(1/2)) + 1

dp = []

for i in range(2,ma_root+1) : # 제곱수 구하기
    if i**2 <= ma :
        dp.append(i**2)

result = []

for num in dp : # 제곱수의 배수 구하기 (소수로 하기..?)
    k = 1
    temp2 = num*k
    while temp2 <= ma :
        temp2 = num * k
        if (mi <= temp2) and (temp2 <= ma) :
            result.append(temp2)
        k+=1

result = set(result)

print(ma-mi+1-len(result))

