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


# 9465 스티커
T = int(input())
result = []
for _ in range(T) :
    n = int(input())
    array = [[],[]]
    array[0] = list(map(int,input().split()))
    array[1]= list(map(int,input().split()))


    dp0, dp1, temp0, temp1 = [0]*n, [0]*n, [0]*n, [0]*n

    dp0[0] = array[0][0]
    dp1[0] = array[1][0]

    temp0[0], temp0[1]  = array[0][0], array[0][0]
    temp1[0], temp1[1] = array[1][0], array[1][0]


    for i in range(1,n) :
        # if cursor == 1 :
            dp0[i] = dp0[i-1] + array[0][i]
            dp1[i] = dp1[i-1] + array[1][i]
            print("dp ----->", dp0, dp1)
            if i > 1 :
                temp0[i] = temp0[i-1] + array[1][i]
                temp1[i] = temp1[i-1] + array[0][i]
            print(temp0, temp1)
        else :
            dp0[i] = dp0[i-1] + array[1][i]
            dp1[i] = dp1[i-1] + array[0][i]
            print("dp ----->", dp0, dp1)
            if cursor == -1  :
                temp0[i] = temp0[i-1] + array[0][i]
                temp1[i] = temp1[i-1] + array[1][i]
            print(temp0, temp1)
        dp0[i] = max(dp0[i], temp0[i])
        dp1[i] = max(dp1[i], temp1[i])


        temp0[i] = dp0[i-1]
        temp1[i] = dp1[i-1]
        print(temp0, temp1)
        print("최종dp ----->",dp0,dp1)


        result.append(max(dp0[i], dp1[i]))
        print("result ---------->", result)
        print('--------------i바뀜---------')

for k in result :
    print(k)



# 9465 스티커
'''
음... 일단 엄청 힘들었고, 대각선으로 선택하고 그 다음 차수의 경우, 앞이 비어있는 경우로 시작하는 경우가 생기는데 
그걸 고려를 안해줘서 계속 틀렸음 
dp[i-2]로 시작하는 경우, dp[i-1]로 싲가하는 경우가 있음 
'''
T = int(input())
result = []
for _ in range(T) :
    n = int(input())
    array = [[],[]]
    dp0, dp1 = [0]*n, [0]*n
    array[0] = list(map(int,input().split()))
    array[1]= list(map(int,input().split()))
    if n == 1 :
        print(max(array[0][0],array[1][0]))
    else :
        dp0[0] = array[0][0] # 위로 끝나는 경우
        dp1[0] = array[1][0] # 아래로 끝나는 경우
        dp0[1] = dp1[0] + array[0][1]
        dp1[1] = dp0[0] + array[1][1]
        result.append(max(dp0[0],dp1[0]))
        result.append(max(dp0[1],dp1[1]))

        if n == 2 :
            print(result[-1])
        else :
            for i in range(2,n) :
                dp0[i] = max(dp1[i-2]+array[0][i],dp1[i-1] + array[0][i])
                dp1[i] = max(dp0[i-2]+array[1][i],dp0[i-1] + array[1][i])
                result.append(max(dp0[i],dp1[i]))
            print(result[-1])

# 2156 포도주 시식
num0 , num1, num2 = [], [], [] # 연결 개수에 따른 배열
array = [] # 포도주

#2156 포도주
n = int(input())
array = []
for _ in range(n) :
    array.append(int(input()))

result = [array[:1],array[:2]]
answer = [array[0],array[0]+array[1]]




for i in range(2,n) :
    temp0, temp1, temp2 = [], [], []
    if result[i-2][-1] != 0 :
        temp0 = result[i-2]+[0]+[array[i]] # 앞이 비어있음
    if (result[i-2][-1] == 0) and (i!=2) :
        temp1 = result[i-2] + [array[i-1]] + [array[i]] # 앞이 비어있지 않음
    if (result[i-1][-2] != 0 and result[i-1][-1] != 0) :
        temp2 = result[i-1] + [0] # 내가 비었음
    if i == 2 :
        temp1 = [0, array[1], array[2]]


    a,b,c = sum(temp0),sum(temp1),sum(temp2)
    answer.append(max(a,b,c))

    print("temp0------>", temp0)
    print("temp1------->", temp1)
    print("temp2------->", temp2)
    if max(a,b,c) == c :
        result.append(temp2)
    elif max(a,b,c) == b :
        result.append(temp1)
    else : result.append(temp0)
    print("result------------->", result)
print(answer[-1])



# 포도주 뿌시기
n = int(input())
array = [] # 포도주

for _ in range(n) :
    array.append(int(input()))

pre = [[array[0],array[1],0],[0,array[1],array[2]],[array[0],0,array[2]]] # 3잔까지 갔을 때 나오는 경우의 수

# for j in range(3,n) :
#     current = []
#     for i in pre :
#         if (i[-1] != 0)and(i[-2] != 0 ) and (i[-3] == 0):
#             current.append(i[1:] + [0])
#         if (i[-1] != 0) and (i[-2] == 0) and (i[-3] != 0):
#             current.append(i[1:] + [array[j]])
#         if (i[-1] == 0) and (i[-2] != 0) and (i[-3] != 0):
#             current.append(i[1:]+[array[j]])
#         if (i[-1] == 0) and (i[-2] != 0) and (i[-3] == 0) :
#             current.append(i[1:]+[array[j]])
#         if (i[-1]!= 0) and (i[-2] ==0) and (i[-3] != 0) :
#             current.append(i[1:] + [0])
#     print("pre------>", pre)
#     print("current----->", current)

    pre = current
result = list(sum(i) for i in current)
print(max(result))


n = int(input())
array = [] # 포도주

for _ in range(n) :
    array.append(int(input()))

yes = [6,16]
no = [0,6]
result =[]
for i in range(2,n) :
    temp_y1 = no[i-3]+array[i-2] + array[i]
    temp_y2 = yes[i-3] + array[i - 2] + array[i]
    temp_y3 = no[i-2] + array[i-1] + array[i]
    temp_n1 = yes[i-2] + array[i-1]
    temp_n2 = no[i-2] +array[i-1]
    print(temp_y1,temp_y2,temp_n1,temp_n2)
    yes.append(max(temp_y1,temp_y2))
    no.append(max(temp_n1, temp_n2))
    print("yes--->",yes)
    print("no----->", no)
    result.append(max(yes[i],no[i]))
    print("result---->", result)


# 포도주 잔 다 깨버릴라..
n = int(input())
array = [] # 포도주

for _ in range(n) : # 포도주 잔 채우기
    array.append(int(input()))

if n == 1 :
    print(array[0])
elif n == 2 :
    print(array[0]+array[1])
else :
    dp = [array[0], array[0]+array[1],max(array[0]+array[1],array[1]+array[2],array[0]+array[2])]

    for i in range(3,n) :
        a = dp[i-3] + array[i-1] + array[i]
        b = dp[i-2] + array[i]
        c = dp[i-1]
        dp.append(max(a,b,c))
    print(dp[n-1])


# 스티커 보내는 날
# T = int(input())
#
# for _ in range(T) :
#     n = int(input())
#     array = [[],[]]
#     dp0, dp1 = [0]*n, [0]*n
#     array[0] = list(map(int,input().split()))
#     array[1]= list(map(int,input().split()))
#
#     if n == 1 :
#         print(max(array[0][0], array[1][0]))
#     elif n == 2 :
#         print(max(array[0][0]+array[1][1], array[0][1]+array[1][0]))
#     else :
#         dp0 = [array[0][0],array[0][1]+array[1][0]]
#         dp1 = [array[1][0], array[0][0]+array[1][1]]
#         result = [max(array[0][0], array[1][0]),max(array[0][0]+array[1][1], array[0][1]+array[1][0])]
#         for i in range(2,n) :
#             temp1 = dp0[i-2] + array[]

# 11053 가장 긴 증가하는 부분 수열 (LIS)

n = int(input())
array = list(map(int,input().split()))
dp = [1]*n
for i in range(1,n) :
    for j in range(i) :
        if array[i] > array[j] :
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))


# 11055 가장 큰 증가 부분 수열
n = int(input())
array = list(map(int,input().split()))
dp = array.copy()

for i in range(1,n) :
    for j in range(i) :
        if array[i] > array[j] :
            dp[i] = max(dp[i],dp[j] + array[i])
print(max(dp))

# 11722 가장 긴 감소하는 부분 수열
n = int(input())
array = list(map(int,input().split()))
dp = [1]*n
for i in range(1,n) :
    for j in range(i) :
        if array[i] < array[j] :
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

# 11054 가장 긴 바이토닉 부분 수열
n = int(input())
array = list(map(int,input().split()))
dpIn = [1]*n
dpDe = [1]*n

for i in range(n) :
    for j in range(i) :
        if array[i] > array[j] :
            dpIn[i] = max(dpIn[i], dpIn[j]+1)
for i in range(n-1,-1,-1) :
    for k in range(n-1,i,-1) :
        if array[i] > array[k] :
            dpDe[i] = max(dpDe[i], dpDe[k]+1)
result = list(dpIn[i]+dpDe[i]-1 for i in range(n))
print(max(result))

#1912 연속합
import sys
n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
dp=[-1000]*(n)
for i in range(1,n+1) : # 몇 개 연속
    for j in range(n-i+1) : # 시작하는 위치
        temp = sum(array[j:j+i])
        dp[i-1] = max(dp[i-1],temp)
print(max(dp))


from collections import deque
n = int(input())
array = list(map(int,input().split()))
dp=[0]*n
for i in range(1,n+1) : # 몇 개 연속
    for j in range(n-i+1) : # 시작하는 위치
        temp=[]
        array2 = deque(array)
        for _ in range(j) :
            array2.popleft()
        for _ in range(i) :
            temp.append(array2.popleft())
        dp[i] = max(dp[i],sum(temp))
print(max(dp))


# 연속합
n = int(input())
array = list(map(int,input().split()))
dp =[]
for i in range(1,n+1) : # 몇 개 연속
    for j in range(n-i+1) : # 시작위치
        current = 0
        for k in range(i) : # 연속하는 거만큼 더해주기
            if k == 0 :
                result = -1000*n
            current += array[j]
            j+=1 # 더할 값들 위치 변경해주기
            result = max(result, current)
    dp.append(result)
print(max(dp)



# 연속합
n = int(input())
array = list(map(int,input().split()))
dp = [array[0]]
for i in range(n-1):
    dp.append(max(dp[i] + array[i+1], array[i+1]))
print(max(dp))


# 2579 계단오르기
n = int(input())
array =[]
for _ in range(n) :
    array.append(int(input()))

dp = [0]*n
dp[0] = array[0]
for i in range(1,n) :
    a = dp[i-1]
    b = dp[i-2] + array[i]
    c = dp[i-3] + array[i-1] + array[i]
    if i == n-1 :
        dp[i] = max(b,c)
    else :
        dp[i] = max(a,b,c)
print(dp[n-1])



n = int(input())
array =[]
for _ in range(n) :
    array.append(int(input()))

dp = [0]*n
dp[0] = array[0]
for i in range(1,n) :
    b = dp[i-2] + array[i]
    c = dp[i-3] + array[i-1] + array[i]
    dp[i] = max(b,c)
print(dp[n-1])


n = int(input())
array =[]
for _ in range(n) :
    array.append(int(input()))

dp = [0]*n
dp[0] = array[0]
if n >= 2 :
    dp[1] = array[0]+array[1]

if n >= 3 :
    for i in range(2,n) :
        b = dp[i-2] + array[i]
        c = dp[i-3] + array[i-1] + array[i]
        dp[i] = max(b,c)
print(dp[n-1])


# 1699 제곱수의 합
n = int(input())
dp = [0]*(n+1)
dp[1] = 1
if n >= 2 :
    dp[2] = 2
    if n >= 3 :
        dp[3] = 3

if n >= 4 :
    count = 2
    for i in range(4,n+1) :
        pre = (count)**2
        if i/(count+1) == count+1 :
            count+=1
        if i/count == count :
            dp[i] = 1
        else :
            dp[i] = dp[i-pre] + 1

print(dp[n])


n = int(input())
dp = [0]*(n+1)
dp[1] = 1
if n >= 2 :
    dp[2] = 2
    if n >= 3 :
        dp[3] = 3

if n >= 4 :
    count = 2
    for i in range(4,n+1) :
        if i/(count+1) == count+1 :
            count+=1
        if i/count == count :
            dp[i] = 1
        else :
            dp[i] = dp[i-4]+1
            for j in range(2,count+1) :
                pre = (j)**2
                dp[i] = min(dp[i],dp[i-pre]+1)

print(dp[n])


# 1699 제곱수의 합
n = int(input())
dp = [0]*(n+1)

for i in range(1,n+1) :
    if int(i**0.5) == i**0.5 :
        dp[i] = 1
    else :
        dp[i] = i
        for j in range(1,i) :
            if (j * j) > i:
                break
            if dp[i] > dp[i - j * j] + 1:
                dp[i] = dp[i - j * j] + 1


print(dp[n])

# 9461 파도반 수열
T = int(input())
for _ in range(T) :
    N = int(input())
    dp = [0, 1, 1, 1, 2, 2]
    if N >= 6 :
        for i in range(6,N+1) :
            dp.append(dp[i-1]+dp[i-5])
    print(dp[N])
