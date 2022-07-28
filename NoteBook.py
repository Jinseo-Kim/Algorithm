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
'''

'''
def solution(scoville, K):
    scoville.sort(reverse = True)
    result = 0

    while True:
        if scoville[-1] >= K:
            return result

        first = scoville.pop()
        second = scoville.pop()
        scoville.append(first + second*2)
        scoville.sort(reverse = True)
        result += 1
'''

# def solution(scoville, K, cnt = 0):
#     heapq.heapify(scoville)
#     root_node = heapq.heappop(scoville)
#     second_node = heapq.heappop(scoville)

#     if root_node >= K:
#         return root_node
#     cnt += 1

#     if root_node + second_node * 2 >= K:
#         return cnt
#     else:
#         heapq.heappush(scoville, root_node + second_node * 2)


# scoville = [1, 2, 3, 9, 10, 12]
# k = 7
# print(solution(scoville, k))


'''
def solution(scoville, K, cnt = 0):
    heapq.heapify(scoville)

    while True:
        root_node = heapq.heappop(scoville)
    
        if root_node >= K:
            break
        elif len(scoville) == 0:
            cnt = -1
            break

        second_node = heapq.heappop(scoville)
        heapq.heappush(scoville, root_node + second_node * 2)
        cnt += 1

    return cnt

scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))
'''


'''
from collections import deque

def dfs(graph, start_node, visited = []):
    visited.append(start_node)

    for node in graph[start_node]:
        if node not in visited:
            dfs(graph, node, visited)
    
    return visited


def bfs(graph, start_node):
    need_visited = deque()
    visited = []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.popleft()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

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
print(bfs(graph, start_node = 'A'))

'''

# 선택 정렬
# 선택 정렬의 전체적인 알고리즘은 앞에서부터 정방향 순환하며 최소값과 현재값의 위치를 변경시켜주는 방식으로 짜여져있음.
# 해당 알고리즘은 정방향으로 진행되며 정렬이 이뤄지기 떄문에 정렬이 진행됨에 따라 비교하려는 배열의 길이가 짧아짐.
# 최솟값을 찾는 방법으로 min의 내장 함수를 이용할 수도 있으나 굳이 내장 함수를 사용하지 않고, 값 비교만을 통해 동작하는 코드를 작성함.
'''
def selection_sort(array):
    for i in range(len(array)):
        minimum = i
        for j in range(i+1, len(array)):
            if array[minimum] > array[j]:
                minimum = j

        if minimum != i:
            array[i], array[minimum] = array[minimum], array[i]

    return print(array)


array = [7, 9, 5, 1, 2, 4, 3, 6, 8]
selection_sort(array)
'''


# 삽입 정렬

# 일차적 단순 구현 insert, pop 사용
# pop을 이용해 데이터를 빼내고 그 앞에서 해당 데이터보다 작다면 해당 위치의 뒤에 삽입
'''
def insertion_sort(array):
    for change_data in range(1, len(array)):
        value = array.pop(change_data)

        for j in range(change_data-1, -1, -1):
            if array[j] < value:
                array.insert(j+1, value)
                break
            elif j == 0:
                array.insert(0, value)
                break

    return print(array)
'''


# 구현 후 인터넷 검색 및 개선 코드
'''
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr

 arr = [7,9,5,1,2,4,3,6,8]
 print(insertion_sort(arr))
 '''


# 개선 코드를 따라서 작성
# 이전 인덱스의 값 vs 비교 위치의 값의 비교로 해당 값보다 크다면 swap을 통해 자리 변경. 거듭하여 j의 값이 0이 될 떄까지 반복. 0이면 종료
# 중요 키포인트는 삽입 정렬에선 거듭할수록 위치를 찾으려는 현재값의 인덱스로부터 이전 인덱스의 값들은 모두 정렬이 되어있다는 점.
# ex) 75241 -> 57241 -> 25741 -> 24571 -> 12457 인덱스의 진행 순서는 1, 2, 3, 4로 인덱스 3을 기준으로 이전 인덱스 값의 정렬을 보면 4를 기준으로 2,5,7의 수는 이미 정렬이 되어 있음.
# 이는 특정 인덱스로부터 삽입 정렬이 진행되기 전 특정 인덱스의 값은 정렬되지 않았으나 이전에 진행된 삽입 정렬의 대상 값들은 이미 정렬이 완료되었음을 확인할 수 있음.
'''
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    
    return print(array)

array = [7,9,5,1,2,4,3,6,8]
insertion_sort(array)
'''


# 버블 정렬
'''
def bubble_sort(array):
    for target in range(len(array), 0, -1):
        for j in range(1,target):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
        print(array)

    return array


array = [7,9,5,1,2,4,3,6,8] # test 1
array = [9,7,8,6,3,4,2,5,1] # test 2
print(bubble_sort(array))
'''

# 퀵 정렬
def quick_sort(array):
    left, right = [], []
    pivot = array[len(array)//2]

    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    
    if left:
        quick_sort(left) # [1]
    if right: # [7,9,5,4,3,6,8] 1. [3] + [4] + right 2. [] + [5] + [7,9,6,8] 3. [] + [6] + [7,9,8] 4. [7,8] + [9] + []
        quick_sort(right) 

    return left + [pivot] + right # [1] + [2] + 


array = [7,9,5,1,2,4,3,6,8] # test 1
quick_sort(array)