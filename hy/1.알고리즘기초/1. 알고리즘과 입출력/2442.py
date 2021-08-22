#2442

import sys

n = int(sys.stdin.readline())

for i in range(1,n+1) :
    l = i*2-1
    print(' '*(n-i)+'*'*l)