# 내적
def solution(a, b):
    n = len(a)
    answer = 0

    for i in range(0, n):
        answer += a[i] * b[i]
    return answer


# 3진법 뒤집기
def solution(n):
    result = []
    while (n // 3 != 0):
        ap = n % 3
        n = n // 3
        result.append(str(ap))
    result.append(str(n))
    result.reverse()
    answer = 0
    for i in range(len(result)):
        answer += int(result[i]) * 3**i
    return answer


# 두 개 뽑아서 더하기
def solution(numbers):
    numbers.sort()
    answer = []
    for i in range(len(numbers)-1): #0,1,2,3
        for j in range(i+1, len(numbers)): #1,2,3,4 / 2,3,4 / 3,4 / 4
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()

    return answer

#
n = 5
answer = [[0 for j in range(i+1)] for i in range(n)]