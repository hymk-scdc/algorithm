# 2021.08.19

# 10828 : 스택
'''
실패 - 시간 초과 
해결 - input = sys.stdin.readline 사용 - 꼭 이렇게 쓸 필요 없음 input 대신에 쓰면 됨
'''
import sys

input = sys.stdin.readline
stack = []
N = int(input())

for i in range(N):
    command = input()
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



m,*l = -1,
for a in[*open(0)][1:]:
    l+=[a[5:m]]*-~-(a[1]<"u"!=print(a<"f"and"10"[l>[]]or a<"q" and (l or[m]).pop()or[len(l),(m,*l)[m]][a>"t"]))




# 9012 - 괄호
# 실패- 틀림 : 뭐가 틀렸는지 말을 좀 해봐
'''
)가 들어왔을 때 앞에 (가 있으면 같이 없애
(는 그냥 들여보내
'''
import sys

N = int(sys.stdin.readline())
for i in range(N):
    stack = []
    PS = list(sys.stdin.readline().rstrip())
    for j in range(len(PS)):
        if PS[j] == "(":
            stack.append("(")
        else:
            try:
                stack[-1] == '('
            except IndexError:  # 비어있을 경우
                stack.append(")")
                continue
            else:  ## () 일 경우
                if stack[-1] == ')':
                    stack.append(")")
                else:
                    stack = stack[:-1]
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


# 10799 : 쇠막대기
'''
(를 만나면
'만난 (의 개수 +1' 번째 ) 를 만날 때까지 만난 숫자 + 1을 더한다

import sys
stick = sys.stdin.readline().rstrip()
stick = stick.replace("()", "1")
num = 0
for i in range(len(stick)):
    mid_num = 0
    meet = 0
    if stick[i] == "(":
        for j in range(i, len(stick)-1):
            if stick[j+1] == '(':
                meet += 1
            elif stick[j+1] == ')':
                if meet == 0:
                    if mid_num != 0:
                        num += mid_num+1
                        break
                    else:
                        continue
                else:
                    meet -= 1
            else:
                mid_num += 1
    else:
        continue
print(num)
'''


# 1406 : 에디터
'''
실패 : 시간 초과
해결 : 
'''
import sys

sent = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline())
cursor = len(sent)
for i in range(M):
    command = sys.stdin.readline().rstrip()
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


# 10845 : 큐
import sys

N = int(sys.stdin.readline())
str = []
for i in range(N):
    command = sys.stdin.readline().rstrip()
    if command[:2] == 'pu':
        str.append(int(command.split()[1]))
    elif command[0] == 'p':
        if len(str) == 0:
            print(-1)
        else:
            print(str[0])
            str = str[1:]
    elif command[0] == 's':
        print(len(str))
    elif command[0] == 'e':
        print(0 if min(len(str), 1) == 1 else 1)
    elif command[0] == 'f':
        try:
            print(str[0])
        except IndexError:
            print(-1)
    elif command[0] == 'b':
        try:
            print(str[-1])
        except IndexError:
            print(-1)


# 1158 : 요세푸스 문제
'''
틀림 - 왜? 왜??왜????
해결 - 어떻게 해결했는지 모름 ㅋㅋ.. try except 말고 그냥 나머지로 한꺼번에 함
'''
import sys
N, K = map(int, sys.stdin.readline().rstrip().split(" "))
circle = [i+1 for i in range(N)]
yo = []
for i in range(N):
    yo.append(circle[(K) % len(circle)-1])
    if K % len(circle) ==0:
        circle = circle[:-1]
    else:
        circle = circle[K % len(circle):] + circle[: K % len(circle)-1]
print("<"+", ".join(map(str, yo))+">")


# 10866 : 덱
'''
333을 입력받아서 바로 list 하면 3, 3, 3으로 들어가서 틀렸었음
'''
import sys
N = int(sys.stdin.readline())
deque = []
for i in range(N):
    temp = []
    command = sys.stdin.readline().rstrip()
    if command[:6] == 'push_f':
        temp.append(command.split(" ")[1])
        deque = temp+deque
    elif command[:6] == 'push_b':
        deque.append(command.split(" ")[1])
    elif command[:5] == 'pop_f':
        if len(deque) > 0:
            print(deque[0])
            deque = deque[1:]
        else:
            print(-1)
    elif command[:5] == 'pop_b':
        if len(deque) > 0:
            print(deque[-1])
            deque = deque[:-1]
        else:
            print(-1)
    elif command[0] == 's':
        print(len(deque))
    elif command[0] == 'e':
        print(0 if min(len(deque), 1) ==1 else 1)
    elif command[0] == 'f':
        if len(deque) > 0:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == 'b':
        if len(deque) > 0:
            print(deque[-1])
        else:
            print(-1)
    else:
        pass
deque = list(map(int, deque))


# 10808 : 알파벳 개수
'''

'''
import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'

S = sys.stdin.readline().rstrip()
count = [0 for i in range(len(alphabet))]

for i in range(len(S)):
    index = alphabet.find(S[i])
    count[index] += 1
print(" ".join(map(str, count)))


# 10809 : 알파벳 찾기
import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'

S = sys.stdin.readline().rstrip()
result = [-1 for i in range(len(alphabet))]

for i in range(len(S)-1, -1 ,-1):
    index = alphabet.find(S[i])
    result[index] = i

print(" ".join(map(str, result)))


# 10820 : 문자열 분석
'''
맞은 것 같은데 틀렸대
'''
import sys
N = sys.stdin.readline().rstrip().split("\n")
refer = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", " "]

result = list([0, 0, 0, 0] for i in range(len(N)))

for i in range(len(N)):
    for j in range(len(refer)):
        for k in range(len(N[i])):
            index = refer[j].find(N[i][k])
            if index != -1:
                result[i][j] += 1
for i in result:
    print(" ".join(map(str, i)))


# 2743 : 단어 길이 재기
'''
뭐... 스택 큐 이용하라고?
'''
import sys
N = sys.stdin.readline().rstrip()
print(len(N))


# 11655 : ROT13
import sys

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sent = list(sys.stdin.readline().rstrip())
result = []

for i in range(len(sent)):
    x = sent.pop()
    if lower.find(x) != -1:
        result.append(lower[(lower.find(x)+13) % len(lower)] )
    elif upper.find(x) != -1:
        result.append(upper[(upper.find(x)+13) % len(upper)] )
    else:
        result.append(x)
result.reverse()

print("".join(result))


# 10824 : 네 수
import sys

nums = sys.stdin.readline().rstrip().split(" ")
print(int("".join(nums[:2])) + int("".join(nums[2:])))


# 11656 : 접미사 배열
import sys

word = list(sys.stdin.readline().rstrip())
word.reverse()
suffix = []
for i in range(len(word)):
    temp = word[:]
    temp.reverse()
    suffix.append("".join(temp))
    word.pop()

suffix.sort()
for i in suffix:
    print(i)