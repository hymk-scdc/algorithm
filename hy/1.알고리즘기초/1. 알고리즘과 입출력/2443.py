import sys

n = int(sys.stdin.readline())

for i in range(1,n+1) :
    l = (n+1-i)*2-1
    print(' '*(i-1)+'*'*l)
    