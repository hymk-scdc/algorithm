# 11655 ROT13

L = list('abcdefghijklmnopqrstuvwxyz')
U = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
N = list('0123456789')

words = list(input())

for i in range(len(words)) :
    if words[i] in L :
        current = (L.index(words[i])+13)%len(L)
        words[i] = L[current]
    elif words[i] in U :
        current = (U.index(words[i])+13)%len(U)
        words[i] = U[current]
    else :
        pass

print(''.join(words))