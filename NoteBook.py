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

# Programmers 네트워크 문제
# ------------------------------------------------ 정답 코드 - -----------------------------------------------
# def solution(n, computers):
#     answer = 0
#     visited = [False for i in range(n)]
#     for com in range(n):
#         if visited[com] == False:
#             DFS(n, computers, com, visited)
#             answer += 1  # DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
#     return answer


# def DFS(n, computers, com, visited):
#     visited[com] = True
#     for connect in range(n):
#         if connect != com and computers[com][connect] == 1:  # 연결된 컴퓨터
#             if visited[connect] == False:
#                 DFS(n, computers, connect, visited)


# print(solution(3, [[1,1,0],[1,1,1],[0,1,1]]))
# ------------------------------------------------------------------------------------------------------------


# ----------------------------------------- 내가 다시 작성 해본 코드 -----------------------------------------
# def solution(n, computers, result = 0):
#     invited = [False for i in range(n)]

#     for com in range(n):
#         if invited[com] == False:
#             dfs(n, computers, invited, com)
#             result += 1

#     return result

# def dfs(n, computers, invited, com):
#     invited[com] = True
#     for i in range(n):
#         if com != i and computers[com][i] == 1:
#             if invited[i] is False:
#                 dfs(n, computers, invited, i)

# print(solution(3, [[1,1,0],[1,1,1],[0,1,1]]))
# ------------------------------------------------------------------------------------------------------------
# from collections import deque

# def solution(participant, completion):
#     answer = []
#     participant = deque(sorted(participant))
#     completion = deque(sorted(completion) + ['0' * (len(participant) - len(completion))])

#     starter = 0
#     finisher = 0

#     for i in range(len(participant)):
#         starter = participant.popleft()

#         if finisher == 0:
#             finisher = completion.popleft()

#         if starter != finisher:
#             answer.append(starter)
#         else:
#             finisher = 0
        
#     return answer


# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
# print(solution(participant, completion))
'''
def solution(n, lost, reserve):
    answer = n-len(lost)
    max_sum = len(reserve)
    chg = True

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = 0
                reserve[j] = 0
                answer += 1
            if reserve[j] not in lost:
                if chg and abs(lost[i]-reserve[j]) == 1:
                    answer += 1
                    max_sum -= 1
                    chg = False
        chg = True
        
    if max_sum < 0:
        answer += max_sum

    return answer

n = 8
lost = [2,3]
reserve = [1,2]
print(solution(n, lost, reserve))
다시 풀어봐야함 set 방식이 꽤 좋은 방법이 있었음
''' 


# def solution(numbers):
#     answer = 0
#     slice_number = [list(str(i)) for i in numbers]
#     for i in range(len(slice_number)):
#         pass
#     return answer

# numbers = [6,10,2]
# print(solution(numbers))

'''
def solution(number, k):
    answer = []
    for num in number:    
        if not answer:
            answer.append(num)
            continue
        print(answer)
        if k > 0:
            while answer[-1] < num:
                print(answer)
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break

        answer.append(num)
    
    return "".join(answer)

number = "4177252841"
k = 4
print(solution(number, k))
'''


# 프로그래머스 그리디
'''
def solution(people, tshirts):
    answer = 0
    max_size = max(tshirts)
    in_stock = ['start'] + [0] * max_size

    for i in tshirts:
        in_stock[i] += 1

    for _ in range(len(people)):
        human_size = people.pop()

        if max_size >= human_size:
            for i in range(human_size, max_size+1):
                if in_stock[i] >= 1:
                    in_stock[i] -= 1
                    answer += 1
                    break

    return answer

people = [1,2,3,4]
tshirts = [2,3,4,5]
print(solution(people, tshirts))
'''


from collections import deque


def solution(booked, unbooked):
    answer = []
    booked = deque(booked)
    unbooked = deque(unbooked)
    current_time = ""

    if booked[0][0] >= unbooked[0][0]:
        current_time = unbooked[0][0]
    else:
        current_time = booked[0][0]
    hh = int(current_time[:2])
    mm = int(current_time[3:5])


    while True:
        if not booked and not unbooked:
            break

        if current_time[3:5] >= "60":
            hh = hh + mm // 60
            mm = mm % 60
            current_time = str(hh) + ":" + str(mm)

        if booked[0][0] <= unbooked[0][0]:
            answer.append(booked[0][1])
            booked.popleft()
        else:
            answer.append(unbooked[0][1])
            unbooked.popleft()

        current_time = str(hh) + ":" + str(mm + 10)
    
    return answer

booked = [["09:10", "lee"]]
unbooked = [["09:00", "kim"],["09:05", "bae"]]

print(solution(booked, unbooked))

