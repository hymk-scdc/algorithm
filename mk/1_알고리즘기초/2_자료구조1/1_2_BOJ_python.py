# 2021.08.19
import time

# 10828 : 스택
# 실패 - 시간 초과
start = time.time()

stack = []
N = int(input(""))

for i in range(N):
    command = input("")
    if command[:2] == 'pu':
        stack.append(int(command.split(" ")[1]))
    elif command[:2] == 'po':
        if len(stack) > 0:
            print(stack[-1])
            stack = stack[:-1]
        else:
            print(-1)
    elif command[:2] == 'si':
        print(len(stack))
    elif command[:2] == 'em':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[:2] == 'to':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

print("time :", time.time() - start)


# 9012 - 괄호
# 실패- 틀림 : 뭐가 틀렸는지 말을 좀 해봐
'''
)가 들어왔을 때 앞에 (가 있으면 같이 없애
(는 그냥 들여보내
'''
N = int(input(""))
for i in range(N):
    stack = []
    PS = list(input(""))
    for j in range(len(PS)):
        if PS[j] == "(":
            stack.append("(")
        else:
            try:
                stack[-1] == '('
            except IndexError:
                stack.append(")")
                continue
            else:
                stack = stack[:-1]
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


# 10799 : 쇠막대기
'''
모르겠는데요
'''


# 1406 : 에디터
'''
실패 : 시간 초과
'''
sent = list(input(""))
M = int(input(""))
cursor = len(sent)
for i in range(M):
    command = input("")
    if command == 'L':
        cursor = max(cursor-1, 0)
    elif command == 'D':
        cursor = min(cursor+1, len(sent))
    elif command == 'B':
        if cursor != 0:
            del sent[cursor-1]
        cursor = max(cursor - 1, 0)
    else:
        sent = sent[:cursor]+list(command.split(" ")[1])+sent[cursor:]
        cursor = cursor+1
print("".join(sent))
