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
계수 정렬
'''
list = [0 for i in range(1000001)]

N = int(input())
for i in range(N):
    num = int(input())
    list[num] = list[num]+1

cnt = 0
while (cnt != N):
    for i in range(1000001):
        if list[i] != 0:
            print(i)
            cnt += 1


'''
퀵 정렬

'''



'''
힙 정렬

'''