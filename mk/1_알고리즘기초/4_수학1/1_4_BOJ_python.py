# 2021.09.21

# 10430 : 나머지
A, B, C = list(map(int, input("").split(" ")))
print((A+B)%C, ((A%C) + (B%C))%C, (A*B)%C, ((A%C) * (B%C))%C, sep="\n")


# 2609 : 최대공약수와 최소공배수
'''
모범 답안) 유클리드 호제법으로 최대공약수 구하기
- a, b의 최대공약수 = b, (a를 b로 나눈 나머지)의 최대공약수

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
'''
def multiply(list):
    result = 1
    for i in list:
        result = result * i
    return int(result)

A, B = list(map(int, input("").split(" ")))

measure = []
divide = 2

while (divide <= A and divide <= B):
    if (A % divide == 0) and (B % divide == 0):
        A = A / divide
        B = B / divide
        measure.append(divide)
    else:
        divide += 1


print(multiply(measure))
print(multiply(measure+[A,B]))


# 1934 : 최소공배수
def multiply(list):
    result = 1
    for i in list:
        result = result * i
    return int(result)

T = int(input(""))

for i in range(T):
    measure = []
    divide = 2

    A, B = list(map(int, input("").split(" ")))

    while (divide <= A and divide <= B):
        if (A % divide == 0) and (B % divide == 0):
            A = A / divide
            B = B / divide
            measure.append(divide)
        else:
            divide += 1

    print(multiply(measure+[A,B]))


# 9613 : GCD 합
def multiply(list):
    result = 1
    for i in list:
        result = result * i
    return int(result)

def gcd(A, B):
    measure = []
    divide = 2

    while (divide <= A and divide <= B):
        if (A % divide == 0) and (B % divide == 0):
            A = A / divide
            B = B / divide
            measure.append(divide)
        else:
            divide += 1

    return multiply(measure)

T = int(input(""))

for i in range(T):
    result = 0
    a = list(map(int, input("").split(" ")))
    for j in range(1, a[0]):
        for k in range(j+1, a[0]+1):
            result += gcd(a[j], a[k])
    print(result)


# 11005 : 진법 변환
N, B = list(map(int, input("").split(" ")))
num = []
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while N >= B:
    ex = N % B
    N = N // B
    if 9 < ex < 36:
        ex = alphabet[ex]
    num.append(ex)
num.reverse()

if 9 < N < 36:
    N = alphabet[N]
print(str(N)+"".join(map(str,num)))


# 2745 : 진법 변환
N, B = list(input("").split(" "))
result = 0
N = N[::-1]
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(N)):
    if N[i] in alphabet[10:]:
        num = alphabet.find(N[i])
    else:
        num = int(N[i])
    result += int(B)**i * num

print(result)


# 1373 : 2진수 8진수
import math
N = list(map(int, input("")))
result = []
for i in range(math.ceil(len(N)/3)):
    for j in range(1, 4):
        N[-(3*i + j)]