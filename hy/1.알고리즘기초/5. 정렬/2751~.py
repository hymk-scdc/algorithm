# 2751 수 정렬하기 2

N = int(input())
li = []
for _ in range(N) :
    n = int(input())
    li.append(n)

'''퀵정렬로 해보기'''
key = 0
start = key
end = len(li) - 1


# def quick(li, key, start, end) :
#     if len(li) <= 1 :
#         return li
#     i = start + 1
#     j = end
#     while i <= j : # 엇갈리는 경우
#         while li[key] >= li[i] :
#             i += 1
#         while True :
#             if (li[key]<=li[j]) and (start < j) :
#                 j -= 1
#             else : break
#
#     li[key], li[j-1] = li[j-1], li[key]
#     return quick(li, key+1, key+1, j-2), quick(li, j, j, end)
#
# quick(result, key, start, end)


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

'''힙 정렬 구현해보기'''