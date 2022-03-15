# 11003 최솟값 찾기
'''
from collections import deque

N, L = map(int, input().split())
As = deque(list(map(int, input().split())))
compare = deque([])
results = []
result = 100000001
ind = L-1

for i in range(L):
    add = As.popleft()
    compare.append(add)
    if result > add:
        ind = L-1
        result = add
    else:
        ind = ind-1
    #print('compare', compare)
    #print('ind', ind, 'result', result)
    results.append(result)


while(As):
    add = As.popleft()
    compare.append(add)
    compare.popleft()

    #print('compare', compare)
    if ind == 0:
        result = min(compare)
        ind = compare.index(result)
        #print('ind', ind, 'result',result)
        results.append(result)
    else:
        if result > add:
            ind = L - 1
            result = add
        else:
            ind = ind - 1
        #print('ind', ind, 'result',result)
        results.append(result)


print(' '.join(list(map(str, results))))
'''

# compare의 맨 앞이 제일 작은 값
from collections import deque

N, L = map(int, input().split())
As = deque(list(map(int, input().split())))

compare = deque([])
compare.append([-1, 1000000001])
results = []

for idx in range(N):
    add = As.popleft()

    while compare and compare[-1][1] > add:
        compare.pop()

    while compare and idx - compare[0][0] >= L:
        compare.popleft()

    compare.append([idx, add])
    #print(compare)
    results.append(compare[0][1])

print(*results)