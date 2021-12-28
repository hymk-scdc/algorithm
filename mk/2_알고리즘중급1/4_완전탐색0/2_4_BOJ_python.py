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


# 10972 : 다음 순열
'''
뒤에서부터 보면서 
'''
N = int(input())
seq = list(map(int, input().split()))
yn = 1

for i in range(-1, -N, -1):
    for j in range(i-1, -N-1, -1):
        if seq[j] < seq[i]:
            seq[j], seq[i] = seq[i], seq[j]
            print(' '.join(map(str, seq[:j+1] + sorted(seq[j+1:]))))
            sys.exit(0)
print(-1)

'''
while로 바꾸기
'''

N = int(input())
seq = list(map(int, input().split()))
yn = 1
i = -1
j = -2

while ((yn == 1) & (i >-N) & (j >-N-1)):
    #print(i, j)
    if seq[j] < seq[i]:
        seq[j], seq[i] = seq[i], seq[j]
        print(' '.join(map(str, seq[:j + 1] + sorted(seq[j + 1:]))))

        '''for i in seq[:j + 1] + sorted(seq[j + 1:]):
            print(i, end=' ')'''
        yn = 0
    j -= 1
    #print(i, j)
    #print('---')

    if j == -N:
        #print('여기', i, j)
        i -= 1
        j = i-1

        #print('여기1', i, j)

if yn == 1:
    print(-1)
