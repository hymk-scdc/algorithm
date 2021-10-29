# 음료수 얼음 얼려먹기

# 데이터 담기
n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # cf. str은 iterable


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        print(x,y)
        return False
    # 방문처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        print("여기가 트루야" , x, y)
        return True
    return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(count)


# 재귀함수 연습
def pr(i) :
    if i >= 10 :
        print(i, "넘음")
    else :
        print(i,"안넘음")
        pr(i+1) # 여기서 1 ~ 10 까지 갔음
        print(i,"돌아와") # 9 ~ 1 까지 다시 돌아감
        pr(i+2) # 근데 9 -> 11 //-> 8 -> 10 //-> 7 -> 9 -> 10 -> 9 -> 11 //








