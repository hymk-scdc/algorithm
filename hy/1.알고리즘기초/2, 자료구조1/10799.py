

# --- 결과 도출 ---
import sys
stack = list(sys.stdin.readline().rstrip())

temp = []
result = 0
pre = None


for i in range(len(stack)) :
    current = stack[i]
    temp.append(current)

    if (pre == ')') & (current == ')') :
        result += 1
        temp.pop()
        temp.pop()
    elif (pre == '(') & (current == ')') :
        temp.pop()
        temp.pop()
        result += len(temp)
    else :
        pass
    pre = current

print(result)