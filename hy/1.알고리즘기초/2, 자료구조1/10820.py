# 10820 문자열 분석

L = list('abcdefghijklmnopqrstuvwxyz')
U = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
N = list('0123456789')

i = 0
while True :
    lower = 0
    upper = 0
    num = 0
    space = 0
    try :
        sentence = list(input()) # sys 하면 rstrip해야 하는데 그거 하면 마지막 공백들이 사라짐
        for j in sentence :
            if j in U :
                upper += 1
            elif j in L :
                lower += 1
            elif j in N :
                num += 1
            else :
                space += 1
        print(lower, upper, num, space)
        i+=1
    except :
        break



