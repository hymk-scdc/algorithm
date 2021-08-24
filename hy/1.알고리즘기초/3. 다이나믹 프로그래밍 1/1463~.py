# 1463
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
