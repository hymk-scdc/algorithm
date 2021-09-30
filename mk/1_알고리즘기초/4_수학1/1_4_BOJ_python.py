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
'''
oct int 내장함수
'''
N = list(map(int, input("")))

result = []
N.reverse()
if len(N) % 3 == 1:
    N = N + [0] * 2
elif len(N) % 3 == 2:
    N = N + [0]

temp = 0
for i in range(len(N)):
    temp += N[i] * (2**(i % 3))
    if i % 3 == 2:
        result.append(temp)
        temp = 0
result.reverse()

print("".join(map(str, result)))


# 1212 : 8진수 2진수
'''
다른 답안) 내장 함수 사용
'''
'''
# 내 답안 : 시간 초과
N = list(map(int, input("")))
N.reverse()

result = []
i = N.pop()
num = [(i // 2) // 2, (i // 2) % 2, i % 2]
index = num.index(1)
result = result + num[index:]
N.reverse()

for i in N:
    num = [(i // 2) // 2, (i // 2) % 2, i % 2]
    result = result + num
print("".join(list(map(str, result))))
'''
print(bin(int(input(), 8))[2:])

# 2089 : -2진수

N = int(input(""))
remain = ''
if N == 0:
    print(0)
    exit()

while (N != 1):
    if N % -2 == 0:
        remain = '0' + remain
        N = N // -2
    else:
        remain = '1' + remain
        N = (N-1) // -2

print(str(N)+remain)


# 11576 : Base Conversion
A, B = list(map(int, input("").split(" ")))
N = int(input(""))
Nums = list(input("").split(" "))
num_ten = 0
for i in range(len(Nums)):
    num_ten += int(Nums[len(Nums)-i-1]) * (A**i)

num = []
while num_ten >= B:
    ex = num_ten % B
    num_ten = num_ten // B
    num.append(ex)
num.reverse()


# 1978 : 소수 찾기
N = int(input(""))
Num = list(map(int, input("").split(" ")))
cnt = 0  # 소수가 아닌 수
for i in Num:
    n = 2
    if i == 1: cnt += 1
    while (n < i):
        if i % n == 0:
            cnt += 1
            break
        n += 1
print(N-cnt)


# 1929 : 소수 구하기
'''
# 시간 초과
# 나누는 수 (n)을 num의 제곱근으로 하면 시간초과 해결됨

M, N = list(map(int, input("").split(" ")))
for num in range(M, N+1):
    n = 2
    if num == 2: 
        print(num)
    while (n < num):
        if num % n == 0:
            break
        if n == num-1:
            print(num)
        n += 1
'''
# 아예 다른 방식 : 미리 채워놓고 프린트하는 방식
# 근데 프린트가 인덱싱이고 채워 넣을 때 계속 확인해서(확인이 시간초과에 영향?) 시간 초과 뜰 줄 알았는데 무슨 차이인지 모르겠음

M, N = list(map(int, input("").split(" ")))
decimal = [0 for i in range(N+1)]
decimal[1] = 1

for i in range(2, (N // 2)+1):
    if decimal[i] == 0:
        for j in range(2, (N // i) + 1):
            decimal[i * j] = 1
    else:
        continue

for i in range(M, N+1):
    if decimal[i] == 0:
        print(i)


# 6588 : 골드바흐의 추측
'''
# 제일 깔끔한 것 같은데 시간초과
decimal = [0 for i in range(1000001)]

decimal_list = []

for i in range(2, 1000001):
    if decimal[i] == 0:
        decimal_list.append(i)
        for j in range(2, (1000000 // i) + 1):
            decimal[i * j] = 1
    else:
        continue

# 이 부분? 고쳤더니 맞게 됐음
def result(n):
    for a in decimal_list:
        try:
            decimal_list.index(n-a)
        except:
            continue
        else:
            str = "%d = %d + %d" % (n, a, n-a)
            return str

while(1):
    n = int(input(""))
    if n == 0:
        exit()
    print(result(n))
'''

decimal = [1 for i in range(1000001)]

for i in range(2, 1000001):
    if decimal[i] == 1:
        for j in range(2, (1000000 // i) + 1):
            decimal[i * j] = 0
    else:
        continue

def result(n):
    for a in range(3, 1000001):
        if decimal[a] & decimal[n-a]:
            str = "%d = %d + %d" % (n, a, n - a)
            return str
        else:
            continue

while(1):
    n = int(input(""))
    if n == 0:
        exit()
    print(result(n))


# 11653 : 소인수분해
N = int(input(""))
n = 2

while(N != 1):
    if N % n == 0:
        print(n)
        N = N // n
    else:
        n += 1


# 10872 : 팩토리얼
result = 1

N = int(input(""))
for i in range(1, N+1):
    result = result * i
print(result)

