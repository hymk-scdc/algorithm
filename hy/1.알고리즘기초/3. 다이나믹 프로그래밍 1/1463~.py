# 1463 
## 21.08.25 다시 풀었는데...좀 더 시간이 필요할 것 같다
import sys
n = int(sys.stdin.readline())
count = 0

while n != 1 :
    if n % 3 == 0 :
        n = n/3
        count += 1
    elif (n-1) % 3 == 0 :
        n -=1
        count += 1
    elif n % 2 == 0 :
        n = n/2
        count += 1
    else :
        n -=1
        count += 1
print(count)

# 11726 2Xn 타일링
import sys
n = int(sys.stdin.readline())
result = 0

def factorial(n) :
    if n == 0 :
        return 1
    return n*factorial(n-1)

a = 0 # 2개짜리 개수
b = 0  # 1개짜리 개수
result = 0


while b >= 0 :
    b = n - 2*a
    temp = factorial(a+b)/(factorial(a)*factorial(b))
    result = result + temp
    a+=1

print(result)


# 11726 다시 풀기 틀림
from math import factorial as fac
import sys

n = int(sys.stdin.readline())
result = 0

a = 0 # 2개짜리 개수
b = n - 2*a  # 1개짜리 개수
result = 0


while b >= 0 :
    result = result + fac(a + b) / (fac(a) * fac(b))
    a += 1
    b = n - 2*a

print(int(result)%10007)

# 11727 일단 pass


# 9095 1,2,3 더하기
import sys
from math import factorial as fac

ns = []
T = int(sys.stdin.readline())
for _ in range(T) :
    ns.append(int(sys.stdin.readline()))


for n in ns :
    num1 = 0 # 1의 개수
    num2 = 0 # 2의 개수
    num3 = 0 # 3의 개수

    num3_max = n//3 # 3의 최대 개수
    num2_max = n//2 # 2의 최대 개수
    results = [] # 조합 담을 곳


    for i in range(num3_max, -1, -1) :
        for j in range(num2_max, -1, -1) :
            if num2*2 + num3*3 > n :
                print(num2,num3)
                break
            for k in range(n,-1,-1) :
                num1, num2, num3  = k, j , i
                if num1 + num2*2 + num3*3 != n :
                    results.append([num1,num2,num3])


    total_sum = 0
    for result in results :
        total = sum(result)
        temp = fac(total) / (fac(result[0])*fac(result[1])*fac(result[2]))
        total_sum = total_sum + temp

    print(int(total_sum))
### 음 ............................... 몰라 ..... 안해 먹어

# # 11052 카드 구매하기
# import sys
#
# n = int(sys.stdin.readline())
# prices = list(map(int, sys.stdin.readline().rstrip().split()))
#
# for price in prices :
#     print

################ 새로운 시작 ###################

# 1463 1로 만들기


n = int(input())

def make1(n) :
    dp = [0, 0, 1, 1] # 0 ~ 3의 답을 미리 담아둠
    if n < 4 :
        return dp[n]
    else :
        for i in range(4,n+1) :
            d1 = i -1 # n에서 1 뺀 값
            if i % 2 == 0 :
                d2 = int(i / 2) # n을 2로 나눈 값
            else : d2 = i-1
            if i % 3 == 0 :
                d3 = int(i / 3) # n을 3으로 나눈 값
            else : d3 = i-1
            temp = min(dp[d1], dp[d2], dp[d3]) # 위의 세 가지 값의 답 중 가장 작은 것 선택
            dp.append(temp+1) # 거기에 1 더하기
        return dp[n]

print(make1(n))


# 11726 2*n 타일링

n = int(input())

def tile(num) :
    dp = [0, 1, 2, 3]
    if num < 4 :
        return dp[num]%10007
    else:
        for i in range(4,num+1) :
            dp.append(dp[i-1] + dp[i-2])
        print(dp)
        return dp[num]%10007
print(tile(n))
<<<<<<< Updated upstream



# 11727 2*n 타일링 2 몰라 몰라!!!!

dp = [0,2,2]
dp2 = [1,3,5]
n = int(input())
if n <= 2 :
    print(dp2[n-1])
else :
    for i in range(3,n+1) :
        dp.append(dp[i-1] + 4)
        dp2.append(dp2[i-1] + dp[i])
    print(dp2[n])

# 9095 1,2,3 더하기

def sum123(n) :
    result = [1,2,4,7]
    if n < 4 :
        return result[n-1]
    else :
        for i in range(4,n) :
            temp = result[i-1] + result[i-2] + result[i-3]
            result.append(temp)
        return result[n-1]
=======

# 11727 2*n 타일링 2
>>>>>>> Stashed changes

T = int(input())

for j in range(T) :
    n = int(input())
    print(sum123(n))


# 11052 카드 구매하기

n = int(input())
p = [0] + list(map(int,input().split()))
dp =[0 for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,i+1) :
        dp[i] = max(dp[i], dp[i-j] + p[j])
print(dp[n])




# 10844 쉬운 계단 수
n = int(input())
num = [1] + [0]*n
count = 0
for j in range(n) :
    for i in range(0,10) :
        if (j == 0) & (i == 0) :
            pass
        if num[j]-1 > -1 :
            num[j+1] = num[j]-1
            count += 1
        else : pass
        if num[j]+1 < 10 :
            num[j+1] = num[j]+1
            count += 1
        else : pass
print(count-1)

n = int(input())
current = [0,1,1,1,1,1,1,1,1,1]
temp = [0]*10

if n == 1 :
    print(sum(current)%1000000000)
else :
    for i in range(1,n) :
        for j in range(10) :
            if j == 0 :
                temp[j] = current[j+1]
            elif j == 9 :
                temp[j] = current[j-1]
            else :
                temp[j] = current[j-1] + current[j+1]
        current = temp.copy()
    print(sum(current)%1000000000)


#11057 오르막 수

n = int(input())
current = [1,1,1,1,1,1,1,1,1,1]
temp = [0]*10

if n == 1 :
    print(sum(current)%10007)
else :
    for i in range(1,n) :
        for j in range(10) :
                temp[j] = sum(current[:j+1])
        current = temp.copy()
    print(sum(current)%10007)


# 2193 이친수
n = int(input())
dp = [0,1] + [0]*(n-1)

if n <= 1 :
    print(dp[n])
else :
    for i in range(2,n+1) :
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
