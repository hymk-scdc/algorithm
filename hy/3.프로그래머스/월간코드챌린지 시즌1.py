# 3진법
def solution(n):
    temp = []
    while True:  # 3진법 거꾸로
        mok = n // 3

        etc = n % 3
        temp.append(etc)
        n = mok

        if mok == 0:
            break

    answer = 0
    gob = 3**(len(temp)-1)
    for i in range(len(temp)):  # 10진법
        answer += gob * temp[i]
        gob = gob//3
    return answer

# 삼각 달팽이

n = int(input())

direct = [-1,0,1] # 아래, 옆, 위

layer= [[[],[]] for _ in range(n+1)]
num = 1
current_layer = 0
current_direct = 0
for i in range(n, 0, -1) :
    for j in range(i) :
        if direct[current_direct] == -1 :
            current_layer += 1
            layer[current_layer][0].append(num)
        elif direct[current_direct] == 0 :
            layer[current_layer][0].append(num)
        else :
            current_layer -=1
            layer[current_layer][1].insert(0, num)
        num += 1
    if current_direct == 2 :
        current_direct = 0
    else :
        current_direct += 1
answer = []
for li in layer :
    answer += li[0]
    answer += li[1]