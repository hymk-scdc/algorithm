# 10430 나머지

a, b, c = map(float, input().split())

print(int((a+b)%c))
print(int(((a%c)+(b%c))%c))
print(int((a*b)%c))
print(int(((a%c)*(b%c))%c))


# 2609 최대공약수와 최소공배수

'''
유클리드 호제법이라는 것이 있더라 
둘의 최대 공약수는 a를 b로 나눈 나머지와 b의 최대 공약수와 같다. 

def gcd(a,b) : 
    while > 0 : 
        a, b = b, a%b
    return a 
'''

a, b = map(int, input().split())

max_num = 0 # 최대공약수

if (a!= 1) and (b!=1) :
    for i in range(1,min(a,b)+1) :
        if (a%i == 0) and (b%i == 0) :
            max_num = i
    min_num = (a // max_num) * b  # 최소공배수

else :
    max_num = 1
    min_num = a * b

print(max_num)
print(min_num)

# 1934 최소공배수
'''
시간초과 났었음 그래서 최대공약수 구하는 for문을 뒤에서부터로 바꿨음
'''
T = int(input())
for _ in range(T) :
    a, b = map(int, input().split())
    for i in range(min(a,b),0,-1) :
        if (a%i == 0) and (b%i == 0) :
            max_num = i
            break
    min_num = (a // max_num) * b  # 최소공배수
    print(min_num)

# 9613 GCD 합 최대공약수의 합
T = int(input())

for _ in range(T) :
   var = list(map(int, input().split()))
   n = var[0]
   result = []
   for i in range(2,n+1) :
       for j in range(1,i) :
           for k in range(min(var[i],var[j]),0,-1) :
               if (var[i]%k == 0) and (var[j]%k ==0) :
                   result.append(k)
                   break
   print(sum(result))


# 11005 진법 변환 2
N, B = map(int, input().split())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []

n = N
count = 0
while n >= B :
    count += 1
    n = n//B

answer = N
for i in range(count,0,-1) :
    temp = answer//(B**i) # 몫
    answer = answer%(B**i) # 나머지
    result.append(temp)
result.append(N%B)

for j in range(len(result)) :
    if 10<= result[j] <= 35 :
        result[j] = alphabet[result[j]-10]
    result[j] = str(result[j])

print(''.join(result))


# 2745 진법 변환

N, B = input().split()
B = int(B)
N = list(N)

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = []

for i in N : # index값 찾기
    result.append(alphabet.find(i))

for j in range(len(result)) : # 해당 자리수의 값 계산해주기
    result[j] = result[j]*(B**(len(result)-j-1))

print(sum(result))

# 1373 2진수 8진수
"""
시간초과 났음 .... 
oct int 내장함수 

"""


num2 = list(input())[::-1]

N = 0
for i in range(len(num2)) :
    N += int(num2[i])*(2**i)

temp = N
result = []
while temp >= 8:
    result.append(str(temp%8))
    temp = temp//8
result.append(str(temp))

result.reverse()

print(''.join(result))

# 새로 다시
num2 = list(input())[::-1]
num2 = list(int(i) for i in num2)
count = 0
result = []
for i in range(0,len(num2),3) :
    N = 0
    try : N = N + num2[i]
    except : pass
    try : N = N + num2[i+1]*2
    except : pass
    try : N = N +num2[i+2]*4
    except : pass
    result.append(str(N))
result.reverse()


print(''.join(result))

# 1212 8진수 2진수

num8 = list(input())
num8 = [int(i) for i in num8]
result = []

for num in num8 :
    mok = num//4
    result.append(str(mok))
    temp = num%4
    mok = mok//2
    result.append(str(mok))
    temp = temp%2
    result.append(str(temp))
index = result.index("1")
result = result[index:]

print("".join(result))


# 2089 -2진수

num = int(input())
mok = num
result = []
while True :
    nam = mok % (-2)
    if nam !=0 :
        mok = mok -1
        nam = 1
    temp = mok // (-2)
    mok = temp
    result.append(str(nam))
    if temp == 0 :
        break
result.reverse()
print("".join(result))


# 11576 Base Conversion

A, B = map(int, input().split())

m = int(input())

numA = list(map(int, input().split()))[::-1]

N = 0
for i in range(len(numA)) :
    N += int(numA[i])*(A**i)

temp = N
result = []
while temp >= B:
    result.append(str(temp%B))
    temp = temp//B
result.append(str(temp))

result.reverse()

print(' '.join(result))


# 1978 소수 찾기
N = int(input())
nums = list(map(int,input().split()))

count = 0
for num in nums :
    if num == 1 :
        pass
    for i in range(2,num+1) :
        if i == num :
            count +=1
        if (num%i == 0) :
            break
print(count)

# 1929 소수 구하기
"""
시간초과
"""
M, N = map(int,input().split())

for num in range(M,N+1) :
    if num == 1 :
        pass
    for i in range(2,num+1) :
        if i == num :
            print(i)
        if (num%i == 0) :
            break

"""
새로해보자구 근데도 시간초과군요 
"""
import sys

M, N = map(int,sys.stdin.readline().rstrip().split())
if M == 2 :
    print(M)
if M%2 == 0 :
    M = M+1

for num in range(M,N+1,2) :
    if num == 1 :
        pass
    for i in range(3,num+1,2) :
        if i == num :
            print(i)
        if (num%i == 0) :
            break

"""
다시 렛츠고 틀렸다고 나옴 
"""
import sys

M, N = map(int,sys.stdin.readline().rstrip().split())
def sosu(M,N) :
    if M == 2:
        print(2)
    if M % 2 == 0:
        M = M + 1

    for num in range(M, N + 1, 2):
        if num == 1:
            pass
        count = 0
        for i in range(3, round((num + 1)**(0.5)+1)):
            if (num % i == 0):
                count +=1
                break
        if count == 0 : print(num)
sosu(M,N)

"""
라스트
"""
import sys

M, N = map(int,sys.stdin.readline().rstrip().split())
def sosu(M,N) :
    if (M==1) & (N==1) :
        pass
    elif M == 1 :
        M = 3
        print(2)
    if M % 2 == 0:
        M = M + 1
    if M >= 2 :
        for num in range(M, N + 1, 2):
            if num == 1:
                pass
            count = 0
            for i in range(3, round((num + 1)**(0.5)+1)):
                if (num % i == 0):
                    count +=1
                    break
            if count == 0 : print(num)
sosu(M,N)

""" 
찐막
"""
import sys

M, N = map(int,sys.stdin.readline().rstrip().split())
def sosu(M,N) :
    for i in range(M, N+1) :
        if i == 1 :
            pass
        elif i == 2 :
            print(2)
        else :
            count = 0
            for j in range(2, int(i**0.5)+2) :
                if i % j == 0 :
                    count +=1
                    break
            if count == 0 :
                print(i)

sosu(M, N)

"""미경이는 배수를 지우는 방식으로 했음"""

# 6588 골드바흐의 추측
"""시간초과"""
'''
sosu = []
for i in range(3,999998,2) :
    count = 0
    for j in range(3, int(i ** 0.5)+1,2):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        sosu.append(i)
while True :
    n = int(input())
    if (n >= 6) & (n%2==0):
        for a in sosu :
            if a > n/2 :
                print("Goldbach's conjecture is wrong.")
                break
            else :
                if (n-a) in sosu :
                    print (f"{n} = {a} + {n-a}")
                    break
                else : pass
    else : break
'''
"""
다시 시작 
아니...분명히 100%까지 떠놓고선 왜 시간초과 뜨냐구요 
"""
'''
def isPrime(num) :
    if num == 1 :
        return False
    elif num == 2 :
        return True
    else :
        count = 0
        for j in range(3, int(num ** 0.5)+1):
            if num % j == 0:
                count += 1
                return False
        if count == 0: return True

sosu = []
for i in range(3,500002,2) :
    if isPrime(i) : sosu.append(i)

while True :
    n = int(input())
    if (n >= 6) & (n%2==0):
        for a in sosu :
            if a <= n/2 :
                if isPrime(n-a):
                    print (f"{n} = {a} + {n-a}")
                    break
                else : pass
            else :
                print("Goldbach's conjecture is wrong.")
                break
    else : break
'''
"""
성공!!!!!!!!!!!!!!!!!!!!!!
"""

sosu = [False for _ in range(1000001)]

for i in range(3,999998,2) :
    count = 0
    for j in range(3, int(i ** 0.5)+1,2):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        sosu[i] = True

import sys
while True :
    n = int(sys.stdin.readline().rstrip())
    if n == 0 : break
    for a in range(3,int(len(sosu)/2),2):
        if sosu[a] and sosu[n-a] :
            print(f"{n} = {a} + {n - a}")
            break
        else : pass


# 11653 소인수분해
"""
"""시간초과"""
n = int(input())

def isPrime(num) :
    if num == 1 :
        return False
    elif num == 2 :
        return True
    else :
        count = 0
        for j in range(3, int(num ** 0.5)+1):
            if num % j == 0:
                count += 1
                return False
        if count == 0: return True


for i in range(2,n+1) :
    if n == 1: break
    if isPrime(i) :
        while n%i == 0 :
            print(i)
            n = n/i
"""
"""재도전"""

n = int(input())
i = 2
while n != 1 :
    if n%i == 0 :
        n = n/i
        print(i)
    else :
        i += 1


# 10872 팩토리얼

import sys
n = int(sys.stdin.readline().rstrip())
result = 1
if n >= 2 :
    for i in range(n,1,-1) :
        result = result * i
print(result)

# 1676 팩토리얼 0의 개수
""" 5의 개수로 하면 더 빨리 짧다"""
import sys
n = int(sys.stdin.readline().rstrip())
result = 1
if n >= 2 :
    for i in range(n,1,-1) :
        result = result * i

count = 0
while result % 10 == 0 :
    result = result // 10
    count +=1
print(count)


# 2004 조합 0의 개수

"""시간초과"""

n, m = map(int, input().split())

if m > (n - m) :
    m = n - m

re_n = 1
re_m = 1
for i in range(n,n-m, -1) :
    re_n = re_n*i
for i in range(m,0, -1) :
    re_m = re_m*i

re = re_n//re_m

count = 0
while re% 10 == 0 :
    count +=1
    re = re//10
print(count)


"""
재도전
성공!
"""
import sys
n, m = map(int, sys.stdin.readline().split())

num_n5 = 0
i = 1
count = -1
while count != 0 :
    count = n//(5**i)
    num_n5 += count
    i +=1

num_n2 = 0
i = 1
count = -1
while count != 0 :
    count = n//(2**i)
    num_n2+= count
    i +=1

num_m5 = 0
i = 1
count = -1
while count != 0 :
    count = m//(5**i)
    num_m5+= count
    i +=1

num_m2 = 0
i = 1
count = -1
while count != 0 :
    count = m//(2**i)
    num_m2+= count
    i +=1


num_k5 = 0
i = 1
count = -1
while count != 0 :
    count = (n-m)//(5**i)
    num_k5+= count
    i +=1

num_k2 = 0
i = 1
count = -1
while count != 0 :
    count = (n-m)//(2**i)
    num_k2+= count
    i +=1

print(min(num_n5-(num_m5+num_k5), num_n2-(num_m2+num_k2)))


# 미경 코드
import math

N, M = map(int, sys.stdin.readline().rstrip().split(" "))


# 숫자를 입력하면 그 숫자까지 2의 개수 세는 함수
def num2(number2):
    cnt2 = 0
    for i2 in range(1, int(math.log2(number2))+1):
        cnt2 += number2 // 2**i2
    return cnt2


def num5(number5):
    cnt5 = 0
    for j5 in range(1, int(math.log(number5, 5))+1):
        cnt5 += number5 // 5**j5
    return cnt5


if M == 0 or N == M:
    print(0)
else:
    # 분자
    x2, x5 = num2(N), num5(N)
    # 분모
    y2, y5 = num2(M)+num2(N-M), num5(M)+num5(N-M)
    print(min(x2-y2, x5-y5))