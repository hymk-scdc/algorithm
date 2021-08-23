# 11656 접미사 배열

word = input()

result = []

n = len(word)

for i in range(n) :
    result.append(word[i:])

result = sorted(result)

for i in result : print(i)