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

# 11052 카드 구매하기
import sys

n = int(sys.stdin.readline())
prices = list(map(int, sys.stdin.readline().rstrip().split()))

for price in prices :
    price*






