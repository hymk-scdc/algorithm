# 10430 나머지

a, b, c = map(float, input().split())

print(int((a+b)%c))
print(int(((a%c)+(b%c))%c))
print(int((a*b)%c))
print(int(((a%c)*(b%c))%c))


# 2609 최대공약수와 최소공배수

a, b = map(int, input().split())

max_num = 0# 최대공약수

if (a!= 1) and (b!=1) :
    for i in range(1,min(a,b)+1) :
        if (a%i == 0) and (b%i == 0) :
            max_num = i
    min_num = (a // max_num) * b  # 최소공배수

else :
    max_num = 1
    min_num = a * b

print(max_num)
print(min_num)

# 1934 최소공배수
'''
시간초과 났었음 그래서 최대공약수 구하는 for문을 뒤에서부터로 바꿨음
'''
T = int(input())
for _ in range(T) :
    a, b = map(int, input().split())
    for i in range(min(a,b),0,-1) :
        if (a%i == 0) and (b%i == 0) :
            max_num = i
            break
    min_num = (a // max_num) * b  # 최소공배수
    print(min_num)

# 9613 GCD 합 최대공약수의 합
T = int(input())

for _ in range(T) :
   var = list(map(int, input().split()))
   n = var[0]
   

