# 10816 - 숫자 카드 2
N = int(input())
Ns = list(map(int, input().split(" ")))
M = int(input())
Ms = list(map(int, input().split(" ")))
Ns.sort()
result = []


def binary(mylist, target, start, end, count=0):
    if start > end:
        if count == 0:
            result.append(0)
        return

    mid = (start + end) // 2
    if mylist[mid] == target:
        i = mid + 1
        count = 1
        while mylist[i] == target:
            count += 1
            i += 1
            if i == N:
                break
        i = mid - 1
        while mylist[i] == target:
            count += 1
            i -= 1
            if i == -1:
                break
        result.append(count)

    elif mylist[mid] < target:
        binary(mylist, target, mid+1, end)
    else:
        binary(mylist, target, start, mid-1)


for i in Ms:
    binary(Ns, i, 0, N-1)

print(' '.join(map(str, result)))


# 11729 : 하노이 탑 이동 순서
N = int(input())

def hanoi(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n-1, start, end, mid)
        #  1개 원하는 고으로 이동
        print(start, end)
        hanoi(n-1, mid, start, end)

print(2**N-1)
hanoi(N, 1, 2, 3) # (N개, 시작하는 곳, 원하는 곳)


# 2261 : 가장 가까운 두 점
n = int(input())
sets = []
for i in range(n):
    sets.append(list(map(int, input().split(' '))))
sets.sort(key=lambda x: x[0])

def dist(a,b):
    return (b[0]-a[0])**2 + (b[1]-a[1])**2


def get_min(start, end):
    # 1 두 점 사이 대표 거리
    if end-start == 1:
        return dist(sets[start], sets[end])
    # 2 세 개일 때 대표 거리
    elif end-start == 2:
        return min(dist(sets[start], sets[start+1]), dist(sets[start+1], sets[end]), dist(sets[start], sets[end]))
    # 3 합치기 (1-1, 1-2 두 가지 경우)
    else:
        min_mid = min(get_min(start, (start+end)//2), get_min((start+end)//2, end))
        set_mid_x, set_mid_y = sets[start+end//2]
        test_sets = []

        # 중간값에서 +- min_mid 사이에 있는 애들만 test_sets에 append
        for i in sets:
            if ((set_mid_x - i[0])**2 < min_mid) or ((set_mid_y - i[1])**2 < min_mid):
                test_sets.append(i)

        ### 여기까지 코드는 set_mid 기준으로만 y 거리 비교 -> 후보키끼리 y 거리 비교해야 하

        # test_sets 내부에서 거리 검사 (단, mid 기준으로 양옆에 있는 점들끼리만)
        for i in range(len(test_sets)):
            for j in range(i+1, len(test_sets)):
                if (set_mid_x - test_sets[i][0]) * (set_mid_x-test_sets[j][0]) <= 0:
                    #print(test_sets[i], test_sets[j], dist(test_sets[i], test_sets[j]))
                    min_mid = min(min_mid, dist(test_sets[i], test_sets[j]))

        return min_mid


print(get_min(0, n-1))



#
K, N = map(int,input().split())

line = []

for _ in range(K) :
    line.append(int(input()))

start = 1
end = max(line)
mid = (start+end)//2

while True :
    cnt = 0
    for i in line :
        cnt += i//mid
    if cnt < N :
        end = mid
        mid = (start + end)//2
    elif cnt > N :
        start = mid
        mid = (start + end)//2
    elif cnt == N:
        while cnt == N :
            cnt = 0
            mid += 1
            for j in line:
                cnt += j // (mid)
        print(mid-1)
        break