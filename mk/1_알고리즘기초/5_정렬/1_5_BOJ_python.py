# 2751 : 수 정렬하기2
'''
정렬 종류 별로 다 구현해보기
'''

'''선택 정렬'''
N = int(input(""))
list = []
for i in range(N):
    list.append(int(input("")))

for i in range(N):
    min = i
    for j in range(i+1, N):
       if list[j] < list[min]:
           min = j
       list[i], list[min] = list[min], list[i]

print(list)

'''삽입 정렬'''
N = int(input(""))
list = []
for i in range(N):
    list.append(int(input("")))

