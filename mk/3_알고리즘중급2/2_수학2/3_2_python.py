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


# 1016 제곱 ㄴㄴ 수
M, max1 = map(int, input().split())

N = int(pow(max1, 1/2))
decimal = [0 for i in range(N+1)]
decimal[1] = 1
decimal_list = []

for i in range(2, (N // 2)+1):
    if decimal[i] == 0:
        for j in range(2, (N // i) + 1):
            decimal[i * j] = 1
    else:
        continue

for i in range(2, N+1):
    if decimal[i] == 0:
        decimal_list.append(i)

result_index = [0 for i in range(max1-M+1)]
for i in decimal_list:
    #print((M//(i**2)),'to', (max1//(i**2)))
    for j in range(max((M//(i**2)),1), (max1//(i**2))+1):
        try:
            result_index[i*i*j-M] = 1
        except:
            pass
        #print(i, j, i*i*j-M)

print(result_index.count(0))

