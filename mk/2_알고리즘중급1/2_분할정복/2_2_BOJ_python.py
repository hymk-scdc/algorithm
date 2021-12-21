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