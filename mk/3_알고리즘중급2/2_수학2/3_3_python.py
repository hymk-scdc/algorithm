# 1629 곱셈
A, B, C = map(int, input().split())

if A > abs(A-C):
    mid = (A-C)**B

else:
    mid = (A**B) % C

print(mid % C)

# ver 2
# 2000000000 10000000 15321531
A, B, C = map(int, input().split())
cnt = 1

R = A % C
results = [R]

while(cnt<B):
    R *= A
    if R >= C:
        R = R % C
    print('cnt',cnt,'R', R)
    print('-----')
    if R in results:
        ind = results.index(R)
        mid = (B-1) % (cnt-ind)
        print('cnt',cnt,'ind',ind,'mid',mid)
        print(results)
        print(results[ind+mid])
        print("-----")
        break
    results.append(R)
    cnt += 1


# ver2 제출용
A, B, C = map(int, input().split())
cnt = 1

R = A % C
results = [R]

while(cnt<B):
    R *= A
    if R >= C:
        R = R % C
    if R in results:
        ind = results.index(R)
        mid = (B-1) % (cnt-ind)
        print(results[ind+mid])
        break
    results.append(R)
    cnt += 1


#
def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % C
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            print('b', b, temp, '*', temp, '%', C)
            return temp * temp % C # b가 짝수인 경우
        else:
            print('b', b, temp, '*', temp, '*', a, '%', C)
            return temp * temp * a % C # b가 홀수인 경우


A, B, C = map(int, input().split())

result = power(A, B)
print(result)


# 2748 피보나치 수 2