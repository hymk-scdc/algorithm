
# 10808 알파벳
import sys


alphabet ='abcdefghijklmnopqrstuvwxyz'
count = [0 for _ in range(len(alphabet))]

word = sys.stdin.readline().strip()

for i in word :
    index = alphabet.find(i)
    count[index] += 1

count = [str(i) for i in count]
print(' '.join(count))

# 10809 알파벳 찾기

import sys


alphabet ='abcdefghijklmnopqrstuvwxyz'
count = [-1 for _ in range(len(alphabet))]

word = sys.stdin.readline().strip()

for i in range(len(word)) :
    index = alphabet.find(word[i])
    if count[index] == -1 :
        count[index] = i

count = [str(i) for i in count]
print(' '.join(count))