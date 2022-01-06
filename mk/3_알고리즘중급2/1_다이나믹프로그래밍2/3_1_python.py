# 2294 동전 2
n, k = map(int, input().split())

results = [0 for i in range(k+1)]
coins = []

for i in range(n):
    coin = int(input())
    coins.append(coin)

if max(coins) > k:
    results = results + [0 for i in range(max(coins)-k)]

for i in coins:
    results[i] = 1

for i in range(min(coins)):
    results[i] = -1

for target in range(1, k+1):
    if (results[target] != 1) and (results[target] != -1):
        compare = []
        for coin in coins:
            if target-coin > 0:
                compare.append(results[target-coin])

        if max(compare) == -1:
            results[target] = -1
        else:
            compare = list(filter(lambda x: x != -1, compare))
            if target == 12:
                print(compare)
            results[target] = min(compare) + 1

    print('target', target, ',result', results)

print(results[k])


# 제출용
n, k = map(int, input().split())

results = [0 for i in range(k+1)]
coins = []

for i in range(n):
    coin = int(input())
    coins.append(coin)

if max(coins) > k:
    results = results + [0 for i in range(max(coins)-k)]

for i in coins:
    results[i] = 1

for i in range(min(coins)):
    results[i] = -1

for target in range(1, k+1):
    if (results[target] != 1) and (results[target] != -1):
        compare = []
        for coin in coins:
            if target-coin > 0:
                compare.append(results[target-coin])

        if max(compare) == -1:
            results[target] = -1
        else:
            compare = list(filter(lambda x: x != -1, compare))
            results[target] = min(compare) + 1

print(results[k])
# 1520 내리막길
