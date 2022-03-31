def dfs(i, j, graph):
    if (i < 0 or j < 0) or (i+1 > n or j+1 > m):
        return
    
    if graph[i][j] == 0:
        graph[i][j] = True

        dfs(i-1, j, graph) # 상
        dfs(i, j-1, graph) # 좌
        dfs(i+1, j, graph) # 하
        dfs(i, j+1, graph) # 우




n, m = map(int,input().split())
result = 0
graph = []

for i in range(n):
    graph.append(list(map(int,input())))    # 얼음 틀

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(f'{i} {j}')
            dfs(i, j, graph)
            result += 1

print(result)