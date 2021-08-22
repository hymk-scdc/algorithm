import sys

stack = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())


temp = []

for _ in range(n):
    com = sys.stdin.readline().strip()
    if (com[0] == "B") & (stack != []):
        stack.pop()
    elif com[0] == 'P':
        stack.append(com[2])
    elif (com[0] == 'D') & (temp != []):
        stack.append(temp.pop())
    elif (com[0] == 'L') & (stack != []):
        temp.append(stack.pop())
    else: pass

print(''.join(stack+list(reversed(temp))))
