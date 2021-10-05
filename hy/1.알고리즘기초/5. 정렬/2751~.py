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


# '''삽입 정렬 코드'''
# def insert(arr) :
#     for end in range(1,len(arr)) :
#         for i in range(end,0, -1) :
#             if arr[i-1] > arr[i] : # arr[i] 정렬의 대상이 되는 요소, arr[i-1] arr[i]의 적절한 위치
#                 arr[i-1], arr[i] = arr[i], arr[i-1]
#     return arr



'''퀵정렬로 해보기'''
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


'''퀵 정렬 코드'''
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


'''병합 정렬'''
N = int(input())
li = []
for _ in range(N) :
    n = int(input())
    li.append(n)

def merge_sort(li) :
    if len(li) < 2 :
        return li

    mid = len(li)//2
    temp1 = merge_sort(li[:mid])
    temp2 = merge_sort(li[mid:])

    result = []
    i, j = 0, 0
    while i < len(temp1) and j < len(temp2) :
            if temp1[i] >= temp2[j] :
                result.append(temp2[j])
                j+=1
            else :
                result[k] = temp1[i]
                i+=1
    result += temp1[i:]
    result += temp2[j:]
    return result

li = merge_sort(li)
for i in li :
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