# 2021.08.17

# 2557 : Hello World
print("Hello World!")


# 1000 : A+B
A = input().split(" ")
print(int(A[0])+int(A[1]))

'''
예제 소스)

a, b = map(int, input().split())
print(a+b)
'''


# 2558 : A+B-2
A = int(input(""))
B = int(input(""))
print(A+B)


# 10950 : A+B-3
T = int(input(""))
for i in range(T):
    A, B = map(int, input("").split(" "))
    print(A+B)


# 10951 : A+B-4
try:
    while(1):
        A, B = map(int, input("").split(" "))
        print(A+B)
except:
    exit()


# 10952 : A+B-5
try:
    while(1):
        A, B = map(int, input("").split(" "))
        if (A==0 and B==0):
            exit()
        else:
            print(A+B)
except:
    exit()


# 10953
T = int(input(""))
for i in range(T):
    A, B = map(int, input("").split(","))
    print(A+B)


# 11021
T = int(input(""))
for i in range(T):
    A, B = map(int, input("").split(" "))
    print("Case #"+str(i+1)+":",A+B)


# 11022
T = int(input(""))
for i in range(T):
    A, B = map(int, input("").split(" "))
    print("Case #{}: {} + {} = {}".format(i+1,A,B,A+B))


# 11718 : 그대로 출력하기
try:
    while(1):
        A = input("")
        print(A)
except:
    exit()


# 11719 : 그대로 출력하기 2
try:
    while(1):
        A = input("")
        print(A)
except:
    exit()

'''
뭐지 위랑 똑같이 했는뎅..
'''


# 11720 : 숫자의 합
N = int(input(""))
num = input("")
sum = 0
for i in range(len(num)):
    sum += int(num[i])
print(sum)


# 11721 : 열 개씩 끊어 출력하기
word = input("")
for i in range(len(word)//10+1):
    if (i==len(word)//10+1):
        print(word[10*i :])
    else:
        print(word[10*i : 10*(i+1)])


# 2741 : N 찍기
N = int(input(""))
for i in range(N):
    print(i+1)


# 2742 : 기찍 N
N = int(input(""))
for i in range(N):
    print(N-i)


# 2739 : 구구단
N = int(input(""))
for i in range(9):
    print("{} * {} = {}".format(N, i+1, N*(i+1)))


# 1924 : 2007년
a, b = map(int, input("").split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', "FRI", "SAT"]
for i in range(a-1):
    b += month[i]
print(day[b % 7])


# 8393 : 합
n = int(input(""))
sum = 0
for i in range(n):
    sum += i+1
print(sum)


# 2021.08.18

# 10818 : 최소, 최대
N = int(input(""))
numbers = list(map(int, input("").split(" ")))
min = numbers[0]
max = numbers[0]
for i in range(1, N):
    if (max < numbers[i]):
        max = numbers[i]
    if (min > numbers[i]):
        min = numbers[i]
print(min, max)


# 2438
N = int(input(""))
for i in range(1, N+1):
    for j in range(i):
        print("*", end='')
    print("")
'''
숏코딩
for i in range(int(input())):print('*'*(i+1))
'''

# 2439
N = int(input(""))
for i in range(1, N+1):
    for j in range(N-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print("")


# 2440
N = int(input(""))
for i in range(N):
    for j in range(N-i):
        print("*", end="")
    print("")


# 2441
N = int(input(""))
for i in range(N):
    for k in range(i):
        print(" ", end="")
    for j in range(N-i):
        print("*", end="")
    print("")


# 2442
N = int(input(""))
for i in range(N):
    for k in range(N-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    if i == N-1:
        break
    print("")


# 2443
N = int(input(""))
for i in range(N, 0, -1):
    for k in range(N-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print("")


# 2444
N = int(input(""))
for i in range(N):
    for k in range(N-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print("")
for i in range(N-1, 0, -1):
    for k in range(N-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print("")


# 2445
N = int(input(""))
for i in range(1,N+1):
    for k in range(i):
        print("*", end="")
    for k in range(2*N-2*i):
        print(' ', end="")
    for k in range(i):
        print("*", end="")
    print()
for i in range(1, N):
    for k in range(N-i):
        print("*", end="")
    for k in range(2*i):
        print(" ", end="")
    for k in range(N-i):
        print("*", end="")
    print("")


# 2446
N = int(input(""))
for i in range(1,N+1):
    for k in range(i-1):
        print(" ", end="")
    for k in range(2*N-2*i+1):
        print("*", end="")
    print("")
for i in range(1,N):
    for k in range(N-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*", end="")
    print("")


# 2522
N = int(input(""))
for i in range(N-1, 0, -1):
    for k in range(i):
        print(" ", end="")
    for k in range(N-i):
        print("*", end="")
    print("")
for i in range(N, 0, -1):
    for k in range(N-i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print("")


# 10991
N = int(input(""))
for i in range(N):
    for k in range(N-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("* ", end="")
    print("")


# 10992
N = int(input(""))
for i in range(1, N):
    for k in range(N-i):
        print(" ", end="")
    print("*", end="")
    if i == 1:
        print("")
        continue
    for k in range(i*2-3):
        print(" ", end="")
    print("*")
for i in range(2*N-1):
    print("*", end="")

