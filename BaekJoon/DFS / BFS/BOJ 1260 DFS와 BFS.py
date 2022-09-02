from collections import deque


def dfs(start, graph, visited_node, result=[]):
    result.append(start)
    visited_node[start] = 1

    for node in graph[start]:
        if visited_node[node] != 1:
            dfs(node, graph, visited_node)

    return result


def bfs(start, graph, visited_node, result=[]):
    result.append(start)
    visited_node[start] = 1
    queue = deque(graph[start])

    while queue:
        node = queue.popleft()

        if visited_node[node] != 1:
            queue.extend(graph[node])
            visited_node[node] = 1
            result.append(node)
    return result


n, m, v = map(int, input().split())
edge_list = [input().split() for _ in range(m)]
# 1부터 노드의 번호가 시작되어 0의 자리에 False값 추가 = v가 인덱스값이 됨.
graph = [False] + [[] for _ in range(n)]
visited_node = [False] + [0] * n   # 해당 노드 방문 여부 확인

for edge in edge_list:
    formatting = list(map(int, edge))
    graph[formatting[0]].append(formatting[1])
    graph[formatting[1]].append(formatting[0])

for node_num in range(1, n+1):
    graph[node_num] = sorted(graph[node_num])

print(*dfs(v, graph, visited_node[:]))
print(*bfs(v, graph, visited_node[:]))
