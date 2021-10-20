# 2751 수 정렬하기 2

'''선택정렬'''
N = int(input())
li = []
for _ in range(N) :
    n = int(input())
    li.append(n)

# min = li[0]
# index = 0
# for i in range(len(li)) :
#     min = li[i] #index만 저장해도 됨
#     for j in range(i+1, len(li)) :
#         if min > li[j] :
#             min = li[j]
#             index = j
#     if min != li[i] :
#         li[i], li[index] = li[index], li[i]
# print(li)


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


'''퀵정렬'''
N = int(input())
li = []
for _ in range(N) :
    n = int(input())
    li.append(n)

# start = 0
# end = len(li) - 1
#
# def quick_sort(li, start, end) :
#     if len(li) == 1 : # 배열 길이가 1 인 경우
#         return li
#     pivot = start
#     left = pivot + 1 # 왼-> 오 시작 지점
#     right = end # 오 -> 왼 시작 지점
#
#     for i in range(left, len(li)) :
#         if li[i] >= li[pivot] :
#             max_li = i
#             print(i)
#             break
#
#     for j in range(right, 0, -1) :
#         if li[j] <= li[pivot] :
#             min_li = j
#             print(j)
#             break
#
#     if max_li <= min_li : # 안 엇갈린 경우
#         li[max_li], li[min_li] = li[min_li], li[max_li]
#     else : # 엇갈린 경우
#         li[pivot], li[min_li] = li[min_li], li[pivot]
#     quick_sort(li, start, min_li-1)
#     quick_sort(li, min_li, end)


'''퀵정렬'''
def quick(li, start, end) :
    if start >= end :
        return
    pivot = start
    left = start + 1
    right = end
    while (left <= right) : # 엇갈리는 경우 전가지 반복
        while (li[pivot] >= li[left] and left <= end) : # 피벗보다 큰 데이터 찾을 때까지 반복
            left += 1
        while (right > start and li[right] >= li[pivot]):# 피벗보다 작은데이터 찾을 때까지 반복
                right -= 1
        if (left > right) : # 엇갈렸다면
            li[right], li[pivot] = li[pivot], li[right]
        else : # 엇갈리지 않았다면
            li[left], li[right] = li[right], li[left]
    quick(li, start, right-1)
    quick(li, right, end)

quick(li, 0, len(li)-1)
print(li)

'''
위에랑 대체 뭐가 다른거지 
시간초과 났음... 파이썬 리스트 기본 정렬이 퀵정렬이라고 함 
'''
N = int(input())
li = []
for _ in range(N) :
    n = int(input())
    li.append(n)

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(li, 0, len(li) - 1)
for i in li :
    print(i)


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




'''병합 정렬'''
'''
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
    result = [0]*len(li)
    i,j= 0, 0
    while (i < len(temp1) and j < len(temp2)) : # 한 쪽이 다 채워지기 전까지
        if temp1[i] < temp2[j] :
            result[k] = temp1[i]
            i += 1
            k += 1
        else :
            result[k] = temp2[j]
            j += 1
            k += 1
    # 마지막까지 채우기 (while문을 for문으로 바꿨음)
    if i == len(temp1) : # i는 다 채워짐
        for z in range(j, len(temp2)) :
            result[k] = temp2[z]
            k += 1
    elif j == len(temp2) : # j가 다 채워짐
        for z in range(i, len(temp1)) :
            result[k] = temp1[z]
            k += 1

    return result

answer = merge_sort(li)

for i in answer :
    print(i)
'''

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





'''
힙 정렬
시간초과
'''

# N = int(input())
# li = []
# for _ in range(N) :
#     n = int(input())
#     li.append(n)
#
#
# def heapify(li) : # 최대힙구조 만들기
#     for i in range(1, len(li)) :
#         child = i
#         while child != 0 :
#             root = (child-1) // 2 # i번째 노드의 부모노드
#             if li[root] < li[child] : # 부모노드보다 자식 노드가 큰 경우
#                 li[root], li[child] = li[child], li[root]
#             child = root
#     return li
#
# def heap_sort(li) :
#     end = len(li) - 1
#     for i in range(end,0, -1) :
#         li[0], li[i] = li[i], li[0] # 가장 큰 값을 가장 마지막으로 보낸다
#         li[:i] = heapify(li[:i])
#
#
# heapify(li)
# heap_sort(li)
#
# for i in li : print(i)


'''이것도 시간초과'''
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


# 11650 좌표 정렬하기
'''시간초과'''

n = int(input())
li = []
for _ in range(n) :
    x, y = map(int, input().split())
    li.append([x,y])

for i in range(n) :
    for j in range(n-1) :
        if li[j][0] > li[j+1][0] :
            li[j], li[j+1] = li[j+1], li[j]
        elif li[j][0] == li[j+1][0] :
            if li[j][1] > li[j+1][1] :
                li[j][1], li[j+1][1] = li[j+1][1], li[j][1]

for k in range(n) :
    print(li[k][0], li[k][1])


'''병합정렬 써볼까 --> 시간초과'''

n = int(input())
li = []
for _ in range(n) :
    x, y = map(int, input().split())
    li.append([x,y])

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

li = merge_sort(li)
for k in range(n) :
    print(li[k][0], li[k][1])


'''
시간초과..pypy3로 하면 맞음 
'''
n = int(input())
li = []
for _ in range(n) :
    a, b = map(int, input().split())
    li.append([a,b])

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
    print (i[0], i[1])

'''
시간초과.. pypy3로 하면 맞음 
'''
n = int(input())
li = []
for _ in range(n) :
    a, b = map(int, input().split())
    li.append([a,b])
li.sort()

for i in li :
    print(i[0], i[1])


# 11651 좌표 정렬하기 2

n = int(input())
li = []
for _ in range(n) :
    a, b = map(int, input().split())
    li.append([b,a])
li.sort()

for i in li :
    print(i[1], i[0])


# 10814 나이순 정렬
n = int(input())
result = []
for i in range(n) :
    age, name = input().split()
    age = int(age)
    result.append([age,i,name])

result.sort()

for j in result :
    print(j[0],j[2])


# 10825 국영수

'''
틀림
int 처리해주니깐 맞았다고 나옴 
'''
n = int(input())

result = []
for _ in range(n) :
    name, ko, en, ma = input().split()
    result.append([ko,en,ma,name])

result.sort(key = lambda x : (-int(x[0]),int(x[1]),-int(x[2]),x[3]))

for j in result :
    print(j[3])


# 10989 수 정렬하기 3
'''메모리 초과 '''
n = int(input())

count = [0] * 10001

for _ in range(n) :
    i = int(input())
    count[i] += 1
result = []
for i in range(10001) :
    if count[i] != 0 :
        for _ in range(count[i]) :
            result.append(i)

for answer in result :
    print(answer)


'''이걸로 해결'''
import sys
n = int(sys.stdin.readline())

count = [0] * 10001

for _ in range(n) :
    i = int(sys.stdin.readline())
    count[i] += 1

for i in range(10001) :
    if count[i] != 0 :
        for _ in range(count[i]) :
            print(i)


'''병합정렬 메로리 초과'''

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

n = int(input())
li = []
for _ in range(n) :
    li.append(int(input()))

li = merge_sort(li)

for i in li : print(i)

'''힙정렬 메모리초과'''
N = int(input())
li = []
for _ in range(N) :
    li.append(int(input()))


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
    for i in range(end,-1, -1) :
        li[0], li[i] = li[i], li[0] # 가장 큰 값을 가장 마지막으로 보낸다
        root = 0
        child = 1
        while child < i :
            child = 2*root + 1
            if child < i-1 and li[child] < li[child+1] :
                child +=1
            if child < i and li[root] < li[child] : # 부모노드보다 자식 노드가 큰 경우
                li[root], li[child] = li[child], li[root]
            root = child

heapify(li)
heap_sort(li)

for i in li : print(i)

'''삽입정렬'''
n = int(input())
li = []
for _ in range(n) : 
    li.append(int(input())) 

def insert_sort(li) :
    for i in range(1,len(li)) :
        for j in range(i,0,-1) :
            if li[j-1] > li[j] :
                li[j-1], li[j] = li[j], li[j-1]
    return li

li = insert_sort(li)
for i in li : print(i)


'''sort()'''
n = int(input())
li = []
for _ in range(n) :
    li.append(int(input()))
li.sort()
for i in li : print(i)


'''버블 정렬 메모리 초과'''
n = int(input())
li = []
for _ in range(n) :
    li.append(int(input()))
    for i in range(len(li)-1,0,-1) :
        if li[i] < li[i-1] :
            li[i], li[i-1] = li[i-1], li[i]
        else :
            break

for i in li : print(i)


# 11652 카드
import sys
n = int(sys.stdin.readline())
li = []
result = []
for _ in range(n) :
    num = int(sys.stdin.readline())
    if num in li :
        for count in result :
            if count[1] == num :
                count[0] +=1
    else :
        li.append(num)
        result.append([1,num])

result.sort(key = lambda x : (-x[0], x[1]))

print(result[0][1])


# 11004 K번째 수
import sys
n, k = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

li.sort()

print(li[k-1])