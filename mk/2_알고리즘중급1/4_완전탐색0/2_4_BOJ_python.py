# 11723 집합
import sys

M = int(input())
S = set()

for i in range(M):
    get = sys.stdin.readline().strip().split()
    if len(get) == 2:
        command, value = get[0], int(get[1])

        if command == 'add':
            S.add(value)

        elif command == 'remove':
            S.discard(value)

        elif command == 'check':
            print(1 if value in S else 0)

        else:
            if value in S:
                S.discard(value)
            else:
                S.add(value)
    else:
        if get[0] == 'all':
            S = set([i for i in range(1, 21)])
            print(S)
        else:
            S = set()
        continue




