# 10430 나머지

a, b, c = map(float, input().split())

print(int((a+b)%c))
print(int(((a%c)+(b%c))%c))
print(int((a*b)%c))
print(int(((a%c)*(b%c))%c))


# 2609 최대공약수와 최소공배수

'''
유클리드 호제법이라는 것이 있더라 
둘의 최대 공약수는 a를 b로 나눈 나머지와 b의 최대 공약수와 같다. 

def gcd(a,b) : 
    while > 0 : 
        a, b = b, a%b
    return a 
'''

a, b = map(int, input().split())

max_num = 0 # 최대공약수

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
   result = []
   for i in range(2,n+1) :
       for j in range(1,i) :
           for k in range(min(var[i],var[j]),0,-1) :
               if (var[i]%k == 0) and (var[j]%k ==0) :
                   result.append(k)
                   break
   print(sum(result))


# 11005 진법 변환 2
N, B = map(int, input().split())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []

n = N
count = 0
while n >= B :
    count += 1
    n = n//B

answer = N
for i in range(count,0,-1) :
    temp = answer//(B**i) # 몫
    answer = answer%(B**i) # 나머지
    result.append(temp)
result.append(N%B)

for j in range(len(result)) :
    if 10<= result[j] <= 35 :
        result[j] = alphabet[result[j]-10]
    result[j] = str(result[j])

print(''.join(result))


# 2745 진법 변환

N, B = input().split()
B = int(B)
N = list(N)

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = []

for i in N : # index값 찾기
    result.append(alphabet.find(i))

for j in range(len(result)) : # 해당 자리수의 값 계산해주기
    result[j] = result[j]*(B**(len(result)-j-1))

print(sum(result))