# list를 활용한 dfs(stack 및 pop)
# 핵심
# 1. while문을 통한 계속된 반복과 종료 조건으로 방문해야할 노드가 없을 때까지 도는 것을 원칙으로 함.
# 2. 맨 끝에 추가된 노드를 pop함으로써 계속하여 맨 끝으로 이동하도록 함. (주의! graph의 데이터는 모두 오름차순으로 정렬되어 있어야 함.)
# 3. 현재 노드가 끝이라는 걸 아는 조건으로는 17번째 열에 해당하며, 이미 방문한 노드가 들어있는 리스트에 현재 방문하고자 하는
#    노드가 있는 지 파악하고 있다면 방문해야할 리스트를 계속 pop하며 최대한 깊이 들어가는 것을 목표로 탐색함.
# 해당 dfs의 특징은 좌 우측 구분 없이 깊이 탐사하는 것을 기준으로 했기에 A-B-D 순이 아닌 A-C-I 순으로 진입함
'''
def dfs(graph, start_node):
    need_visited, visited = list(), list()

    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)

            need_visited.extend(graph[node])
        
    return visited
'''

# 재귀형 dfs 탐색
# 스택 기반이라고 생각하면 이해하기가 편함
# 모든 재귀함수의 종료 조건은 해당 for문을 모두 회전하고(방문할 노드가 없을 때) 종료가 되며 리턴값으로 visited 결과값을 되돌려 줌
'''
def dfs_recursive(graph, start, visited=[]):
    ## 데이터를 추가하는 명령어 / 재귀가 이루어짐
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited


graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']
'''


def solution(n, computers, result = []):
    for i in range(n):
        if computers[i] not in result:
            result.append(i)
            solution(n, computers[i], result)


n = 3
computers = [[1,1,0],[1,1,0],[0,0,1]]