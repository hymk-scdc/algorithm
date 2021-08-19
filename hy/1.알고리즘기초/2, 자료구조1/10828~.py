import sys
N = int(sys.stdin.readline())
stack = []


def push(x):
    stack.append(x)


def pop():
    try:
        print(stack.pop())
    except:
        print(-1)


def size():
    print(len(stack))


def empty():
    if not stack:  # 빈 리스트 False임 따라서, 빈 리스트가 아니면,
        print(0)
    else:
        print(1)


def top():
    try:
        print(stack[-1])
    except:
        print(-1)


for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    else:
        top()