'''
정렬 종류 별로 다 구현해보기
'''

N = int(input(""))
list = []
for i in range(N):
    list.append(int(input("")))

'''
선택 정렬
- 정렬 안 된 부분의 최솟값 <-> 정렬 안 된 부분의 맨 처음값
'''
for i in range(N):
    min = i
    for j in range(i+1, N):
       if list[j] < list[min]:
           min = j
       list[i], list[min] = list[min], list[i]

print(list)

'''
삽입 정렬
- 정렬 안 된 부분의 맨 처음값을 정렬된 부분의 적절한 위치에 삽입
'''
for i in range(1, N):
    for j in range(i, 0, -1):
        if list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
        else:
            break

'''
버블 정렬
- 인접한 원소끼리 차례대로 순서 바꾸기
'''
for i in range(N-1, 0, -1):
    for j in range(1, i+1):
        if list[j-1] > list[j]:
            list[j], list[j-1] = list[j-1], list[j]

'''
병합 정렬
- 분할 정복 알고리즘의 하나
- 분할 : 같은 크기의 2개의 부분 배열로 분할
- 정복 : 부분 배열을 정렬
- 결합 : 정렬된 부분 배열을 하나의 배열에 병합 (병합은 작은 수 선택하며 정렬하면서 병합임)

리스트 길이가 2의 거듭제곱꼴이 아닌 경우는?
'''
import math

# 두개의 리스트를 받아서 병합하는 함수, 각 리스트는 정렬 되어있다고 가정
def merge(list1, list2):
    result = []
    i1 = 0
    i2 = 0
    while((i1 < len(list1)) and (i2 < len(list2))):
        if list1[i1] < list2[i2]:
            result.append(list1[i1])
            i1 += 1
        else:
            result.append(list2[i2])
            i2 += 1
    if (i1 < i2):
        result = result + list1[i1:]
    else:
        result = result + list2[i2:]
    return result

for i in range(int(math.log2(len(list)))):
    for j in range(0, len(list), 2**(i+1)):
        list[j:j+2**(i+1)] = merge(list[j:j+2**i], list[j+2**i:j+2**(i+1)])


'''
퀵 정렬
'''

def quick_sort(list):
    pivot = 0
    low = 0
    high = len(list)-1

    while (low <= high):
        while (list[low] < list[pivot] and low < len(list)-1) :
            low += 1
        while (list[high] > list[pivot]):
            high -= 1
        list[high], list[low] = list[low], list[high]
        low += 1
        high -= 1
    list[pivot], list[high] = list[high], list[pivot]
    return list[:high], list[low:]

# 구글링
def quick(list, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while (left <= right):
        while (left <= end and list[left] <= list[pivot]):
            left += 1
        while (right >= start and list[right] >= list[pivot]):
            right -= 1
        if (left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            list[pivot], list[right] = list[right], list[pivot]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            list[left], list[right] = list[right], list[left]

    quick(list, start, right-1)
    quick(list, right + 1, end)

quick(list, 0, len(list)-1)
print(list)

'''
힙 정렬
'''


# 2751 : 수 정렬하기 2
'''
계수 정렬로 성공
'''
import sys
list1 = [0 for i in range(2000001)]

N = int(sys.stdin.readline())
for i in range(N):
    num = int(sys.stdin.readline())
    list1[num+1000000] += 1

cnt = 0

while cnt != N:
    for i in range(2000001):
        if list1[i] != 0:
            print(i-1000000)
            cnt += 1


# 11650 : 좌표 정렬하기
N = int(input(""))
X = [0 for i in range(200001)]
Y = [[] for i in range(200001)]
# X에는 인덱스에 0,1 표시
# Y에는 대응 인덱스에 넣기
for i in range(N):
     x, y = list(map(int, input("").split(" ")))
     X[x+100000] += 1
     Y[x+100000].append(y)

cnt = 0

while cnt != N:
    for i in range(200001):
        if X[i] != 0:
            Y[i].sort()
            for j in Y[i]:
                print(i-100000, j)
                cnt += 1


# 11651 : 좌표 정렬하기 2
'''
다들 sort 씀
'''
N = int(input(""))
X = [[] for i in range(200001)]
Y = [0 for i in range(200001)]
# X에는 인덱스에 0,1 표시
# Y에는 대응 인덱스에 넣기
for i in range(N):
     x, y = list(map(int, input("").split(" ")))
     Y[y+100000] += 1
     X[y+100000].append(x)

cnt = 0

while cnt != N:
    for i in range(200001):
        if Y[i] != 0:
            X[i].sort()
            for j in X[i]:
                print(j, i-100000)
                cnt += 1


# 10814 : 나이순 정렬
'''
다들 sort 씀
'''
N = int(input(""))
age_name = [[] for i in range(201)]

for i in range(N):
    age, name = input("").split(" ")
    age_name[int(age)].append(name)

cnt = 0

while cnt != N:
    for i in range(201):
        if age_name[i]:
            for j in age_name[i]:
                print(i, j)
                cnt += 1

# 10825 : 국영수
N = int(input(""))
name = []

for i in range(N):
    n, n1, n2, n3 = input("").split(" ")
    name.append([n, int(n1), int(n2), int(n3)])

name = sorted(name, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in name:
    print(i[0])


# 10989 : 수 정렬하기 3






# 11652 : 카드
n = int(input())
result = {}

for case in range(n):
    a = int(input())
    if a in result:
        result[a] += 1
    else:
        result[a] = 1

result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])



# 11004 : K번째 수
'''
이게 맞나..
'''
N, K = input().split(" ")
a = list(map(int, input().split(" ")))

a.sort()
print(a[int(K)-1])


# 1377 : 버블 소트
N = int(input(""))
list_1 = []

for i in range(N):
    list_1.append(int(input()))

for i in range(1,N+2):
    TF = False
    for j in range(1, N):
        if (list_1[j] > list_1[j+1]):
            TF = True
            list_1[j], list[j+1] = list[j+1], list_1[j]
    if TF == False:
=======
'''
pypy 말고 Python3으로 했더니 됨
'''
import sys

N = int(sys.stdin.readline())
a = [0] * 10001

for _ in range(N):
    a[int(sys.stdin.readline())] += 1

for i in range(10001):
    if a[i] != 0:
        for _ in range(a[i]):
            print(i)


# 11652 : 카드


>>>>>>> Stashed changes
