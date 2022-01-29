# 1916 최소비용 구하기

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]


for i in range(m) :
    a,b,c = map(int,input().split()) # 출발도시, 도착도시, 버스비용
    graph[a].append((b,c))

start, end = map(int,input().split())

''' 
지나간 경로에 최소 비용을 계속 업데이트 해주면 될 거 같은데
잘 모르겠음 
'''

# result = []
# def dfs(s, fee) :
#     if s == end :
#         result.append(fee)
#         return
#
#     for i in range(len(graph[s])) :
#         dfs(graph[s][i][0],fee+graph[s][i][1])
#
#
# dfs(1, 0)
# print(min(result))


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]


for i in range(m) :
    a,b,c = map(int,input().split()) # 출발도시, 도착도시, 버스비용
    graph[a].append((b,c))

start, end = map(int,input().split())

visited = [0] * (n+1)
result = []
def dfs(start, fee) :
    if start == end :
        result.append(fee)
        return
    if visited[start] == 1 :
        return
    else :
        visited[start] = 1
        for i in range(len(graph[start])) :
            dfs(graph[start][i][0], fee + graph[start][i][1])

dfs(start,0)

print(min(result))




n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]


for i in range(m) :
    a,b,c = map(int,input().split()) # 출발도시, 도착도시, 버스비용
    graph[a].append((b,c))

start, end = map(int,input().split())

result = []
def dfs(start, fee, li) :
    if start == end :
        result.append(fee)
        return
    if start in li :
        return
    else :
        for i in range(len(graph[start])) :
            dfs(graph[start][i][0], fee + graph[start][i][1], li +[start])

dfs(start,0,[])

print(min(result))


# 다익스트라 알고리즘 구현

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]


for i in range(m) :
    a,b,c = map(int,input().split()) # 출발도시, 도착도시, 버스비용
    graph[a].append((b,c))

start, end = map(int,input().split())

result = [1000000000]*(n+1)

def base(s) : # 연결된 비용 채우기
    for city, fee in graph[s] :
        result[city] = fee


def dijkstar(s) :
    result[s] = 0
    li_idx = [ i for i in range(n+1) ]
    li_idx.remove(0)
    li_idx.remove(s)

    while li_idx :
        # 방문하지 않은 애들 중에서 최소인 것을 선택
        min_idx = 0
        for idx in li_idx :
            if result[min_idx] >= result[idx] :
                min_idx = idx
        temp_fee = result[min_idx]

        # 선택된 최소를 거쳐서 다른 데로 가는 비용들을 갱신해주기
        for city, fee in graph[min_idx] :
            result[city] = min(result[city], fee + temp_fee)
        # 방문처리
        li_idx.remove(min_idx)

base(start)
dijkstar(start)

print(result[end])


