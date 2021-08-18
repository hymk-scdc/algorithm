#2557
print("Hello World!")


#1000
a, b = map(int, input().split())
print(a+b)

# 2558 
a = int(input())
b = int(input())
print(a+b)

# 10950
T = int(input())
for i in range(T) : 
    a, b = map(int, input().split())
    print(a+b)


# 10951
try : 
    while True : 
            a, b = map(int, input().split())
            print(a+b)

except : 
    pass



#10952 
while True : 
    a, b = map(int, input().split())
    if a != 0 : 
        print(a+b)
    else : 
        break 


# 10953
T = int(input())

for i in range(T) : 
    a, b = map(int, input().split(','))
    print(a+b)


# 11021
T = int(input())
for i in range(T) : 
    a, b = map(int, input().split())
    print("Case #{}: {}".format(i+1, a+b))    


# 11022 
T = int(input())
for i in range(T) : 
    a, b = map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i+1, a, b, a+b))


# 11718 
while True : 
    try : 
        print(input())
    except : 
        break


# 11719
while True : 
    try : 
        print(input())
    except : 
        break

# 11720
N = int(input())
n = input()
li = list(int(i) for i in n)
sum(li)
