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
다시 렛츠고 
"""
import sys

M, N = map(int,sys.stdin.readline().rstrip().split())


