# 음료수 얼음 얼려먹기

# 데이터 담기
n,m = map(int, input().split())

data = [['1']*(m+1)]
for _ in range(n) :
    data.append(['1']+list(input()))

# 연결표시
graph = [[set()]*(m+1)]*(n+1)
for i in range(1,n) :
    for j in range(1,m) :
        if data[i][j] == '0' and data[i][j+1] == '0' :
            graph[i][j].add((i,j+1))
        if data[i][j] == '0' and data[i][j-1] == '0' :
            graph[i][j].add((i,j-1))

for j in range(1,m) :
    for i in range(1,n) :
        if data[i][ j] == '0' and data[i+1][ j] == '0':
            graph[i][j].add((i+1,j))
        if data[i][ j] == '0' and data[i-1][ j] == '0':
            graph[i][j].add((i-1,j))

visited = [['False']*(m+1)]*(n+1)

# DFS
def dfs(data, graph, n, m, visited):
    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if data[i][j] == '0':
                visited[i][j] = True
                print(i, j)
                for node in graph[i][j] :
                    node_i, node_j = node[0], node[1]
                    print("여기--->", node_i,node_j)
                    if visited[node_i][node_j] == False :
                        dfs(data,graph, node_i, node_j, visited)
                        return visited








