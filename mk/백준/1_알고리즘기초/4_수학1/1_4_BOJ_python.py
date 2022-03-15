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

# 소수 채우기
decimal = [1 for i in range(1000001)]

for i in range(2, 1000001):
    if decimal[i] == 1:
        for j in range(2, (1000000 // i) + 1):
            decimal[i * j] = 0
    else:
        continue

# 소수 합 찾기
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

while N != 1:
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


# 1676 : 팩토리얼 0의 개수
result = 1

N = int(input(""))
for i in range(1, N+1):
    result = result * i
n = 0
result = list(str(result))
while result.pop() == '0':
    n += 1

print(n)


# 2004 : 조합 0의 개수
'''
# 시간 초과
N, M = map(int, sys.stdin.readline().rstrip().split(" "))

if N//2 < M:
    M = N-M

result1 = 1
for i in range(N-M+1, N+1):
    result1 = result1 * i

result2 = 1
for j in range(1, M+1):
    result2 = result2 * j

n = 0
result = list(str(result1//result2))
while result.pop() == '0':
    n += 1

print(n)
'''
import math
import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

def num2(number2):
    cnt2 = 0
    for i2 in range(1, int(math.log2(number2))+1):
        cnt2 += number2 // (2**i2)
    return cnt2

def num5(number5):
    cnt5 = 0
    for j5 in range(1, int(math.log(number5, 5))+1):
        cnt5 += number5 // (5**j5)
    return cnt5

if M == 0 or N == M:
    print(0)
else:
    # 분자
    x2 = num2(N)
    x5 = num5(N)
    # 분모
    y2 = num2(M)+num2(N-M)
    y5 = num5(M)+num5(N-M)
    print(min(x2-y2, x5-y5))



# 학영

# 선택 정렬
for i in range(len(li)) :
    min_index = i #index만 저장해도 됨
    for j in range(i+1, len(li)) :
        if li[min_index] > li[j] :
            min_index = j
    if min_index != i:
        li[i], li[min_index] = li[min_index], li[i]
print(li)

'''버블 정렬'''
def bubble(li) :
    for _ in range(len(li)) :
        for i in range(1,len(li)) :
            if li[i-1] > li[i] :
                li[i-1], li[i] = li[i], li[i-1]
    return li

'''삽입 정렬'''
def insert_sort(li) :
    for i in range(1,len(li)) :
        for j in range(i,0,-1) :
            if li[j-1] > li[j] :
                li[j-1], li[j] = li[j], li[j-1]
    return li

'''퀵 정렬 다시 구현해보기'''
start = 0 # 첫 인덱스
end = len(li)-1 # 마지막 인덱스
def quick(li, start, end) :
    if start >= end : # 꼭 부등호를 이상으로 해줘야 함
        return
    pivot = start # 처음에 피벗은 젤 첫 원소로 설정한다
    left = start +1 #
    right = end # 오->왼 시작하는 지점

    while left <= right : # 엇갈리기 전까지
        while (li[left] <= li[pivot] and left <= end) :  # 왼->오
            left += 1
        while (li[right] >= li[pivot] and right>start) : # 오->왼
            right -= 1
        if left < right : # 엇갈리지 않았다면
            li[left], li[right] = li[right], li[left]
        elif left > right: # 엇갈렸다면 그 중 작은 값이랑 피벗 바꿔줌
            li[pivot], li[right] = li[right], li[pivot]
    # 그 다음에는 right 위치를 기준으로 분할해서 quick 수행
    quick(li,start,right-1)
    quick(li,right+1,end)


'''k안쓰고 병합정렬'''

N = int(input())
li = []
for _ in range(N) :
    n = int(input())
    li.append(n)

def merge_sort(li) :
    if len(li) < 2 : # 리스트가 1 인 경우
        return li
    mid = len(li)//2

    temp1, temp2 = [], []
    for num in range(mid) :
        temp1.append(li[num])

    for num in range(mid,len(li)) :
        temp2.append(li[num])

    # 합치기 전 아이들도 병합정렬이 되어 있는 상태여야 함
    temp1 = merge_sort(temp1)
    temp2 = merge_sort(temp2)

    # 병합 정렬한 결과물 담을 곳
    result = []
    i,j= 0, 0
    while (i < len(temp1) and j < len(temp2)) : # 한 쪽이 다 채워지기 전까지
        if temp1[i] < temp2[j] :
            result.append(temp1[i])
            i += 1
        else :
            result.append(temp2[j])
            j += 1

    # 마지막까지 채우기 (while문을 for문으로 바꿨음)
    if i == len(temp1) : # temp1는 다 채워짐
        for z in range(j, len(temp2)) :
            result.append(temp2[z])

    elif j == len(temp2) : # temp2가 다 채워짐
        for z in range(i, len(temp1)) :
            result.append(temp1[z])


    return result

answer = merge_sort(li)

for i in answer :
    print(i)

'''힙정렬'''
N = int(input())
li = []
for _ in range(N) :
    n = int(input())
    li.append(n)


def heapify(li) : # 최대힙구조 만들기
    for i in range(1, len(li)) :
        child = i
        while child != 0 :
            root = (child-1) // 2 # i번째 노드의 부모노드
            if li[root] < li[child] : # 부모노드보다 자식 노드가 큰 경우
                li[root], li[child] = li[child], li[root]
            child = root
    return li

def heap_sort(li) :
    end = len(li) - 1
    for i in range(end,0, -1) :
        li[0], li[i] = li[i], li[0] # 가장 큰 값을 가장 마지막으로 보낸다

        child = i-1
        while child != 0 :
            root = (child-1) // 2
            if li[root] < li[child] : # 부모노드보다 자식 노드가 큰 경우
                li[root], li[child] = li[child], li[root]
            child = root

heapify(li)
heap_sort(li)

for i in li : print(i)


'''계수 정렬'''
def gaesu(li, n) :
    num = [0] * (n+1)
    for i in li :
        num[i]+=1
    result = []
    for j in range(len(num)) :
        if num[j] !=0 :
            for _ in range(num[j]) : result.append(j)
    return result