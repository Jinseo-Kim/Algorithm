# list를 활용한 dfs(stack 및 pop)
# 핵심
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
'''
def quick_sort(array):
    same, left, right = [], [], []
    pivot = array[len(array)//2]

    for i in array:
        if i == pivot:
            same .append(i)
        if i < pivot:
            left.append(i)
        if i > pivot:
            right.append(i)
    
    if left:
        left = quick_sort(left) # [1]
    if right: # [7,9,5,4,3,6,8] 1. [3] + [4] + right 2. [] + [5] + [7,9,6,8] 3. [] + [6] + [7,9,8] 4. [7,8] + [9] + []
        # [7] + [8] + []
        right = quick_sort(right) 

    return left + same + right # [1] + [2] + 


array = [7,9,5,1,2,4,3,6,8,2,3] # test 1
print(quick_sort(array))
'''


'''
def solution(id_list, report, k):
    id_dict = dict()
    suspension_count = dict()
    for id in id_list:
        id_dict[id] = set()
        suspension_count[id] = 0
    
    for re in report:
        from_user, to_user = map(str, re.split())
        id_dict[from_user].add(to_user)
    
    id_dict_values = id_dict.values()

    for bad_users in id_dict_values:
        for bad_user in bad_users:
            suspension_count[bad_user] += 1
        
    mail_list = [0 for _ in range(len(id_list))]
    count = 0
    for send_mail in id_dict_values:
        for user in send_mail:
            if suspension_count[user] >= k:
                mail_list[count] += 1
        count += 1
    return mail_list


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
print(solution(id_list, report, k))
'''


# def solution(seoul):
#     answer = 0
#     for i in range(len(seoul)):
#         if seoul[i] == 'Kim':
#             answer = i
#             break

#     return '김서방은 {answer}에 있다'


# seoul = ["Jane", "Kim"]
# print(solution(seoul))


# dfs 수정 (딕셔너리 자료구조 x)
'''
def dfs(start_node, input_nodes, checked_list, result = []):
    result.append(start_node)
    checked_list[start_node] = 1

    search_nodes = input_nodes[start_node]

    for node in search_nodes:
        if checked_list[node] != 1:
            dfs(node, input_nodes, checked_list, result)
    
    return [result, checked_list]



start_node = 1
input_nodes = [[1,3], [0,4,2], [1,4], [0,4], [1,3]]
checked_list = len(input_nodes) * [0]
print(dfs(start_node, input_nodes, checked_list))
'''




# bfs 수정(딕셔너리 자료구조 x)
'''
from collections import deque

def bfs(start_node, input_nodes, checked_list):
    queue = deque(input_nodes[start_node])
    result = [start_node]
    checked_list[start_node] = 1

    while queue:
        start_node = queue.popleft()
        if checked_list[start_node] != 1:
            result.append(start_node)
            checked_list[start_node] = 1

            queue.extend(input_nodes[start_node])

    return [result, checked_list, start_node]



start_node = 0
input_nodes = [[1,3], [0,4,2], [1,4], [0,4], [1,3]]
checked_list = len(input_nodes) * [0]

print(bfs(start_node, input_nodes, checked_list[:]))
print(dfs(start_node, input_nodes, checked_list[:]))
'''


'''def solution(s):
    s = s.lower()
    str_p = 0
    str_y = 0
    for i in s:
        if i == 'p':
            str_p += 1
        if i == 'y':
            str_y += 1

    if str_p == str_y or (str_p == 0 and str_y == 0):
        return True
    return False
'''
'''
def solution(d, budget):
    d.sort()
    print(d)
    length = len(d)
    for i in range(length):
        budget -= d[i]
        if budget < 0:
            return i
    return length

d = [1, 3, 2, 5, 4]
budget = 9
print(solution(d, budget))
'''
'''
def solution(n, words):
    answer = []
    table = dict()
    
    for i in range(len(words)):
        if i == 0:
            table[words[i][0]] = []
        if i != 0:
            if words[i-1][-1] == words[i][0]:
                table[words[i][0]] = []
            else:
                if (i+1) % n == 0:
                    return [n, (i+1)//n+1]
                else:
                    return [(i+1)%n, (i+1)//n+1]

    for i in range(len(words)):
        if table.get(words[i][0]) == []:
            table[words[i][0]].append(words[i])

        elif table.get(words[i][0]) and table.get(words[i][0]) == [words[i]]:
            if (i+1) % n == 0:
                return [n, (i+1)//n]
            else:
                return [(i+1) % n, (i+1)//n]
        
        
        print(table)
        


words = ["tank", "kick", "know", "wheel",
         "land", "dream", "mother", "robot", "tank"]
n = 3
print(solution(n, words))
'''
'''
def gen_combinations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in gen_combinations(rest_arr, n-1):
            result.append([elem]+C)

    return result

print(gen_combinations([0,1,2,3],3))
'''

# def gen_permutations(arr, n):
#     result = []

#     if n == 0:
#         return [[]]

#     for i, elem in enumerate(arr):
#         for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
#             result += [[elem]+P]

#     return result


# arr = [0, 1, 2, 3]

# print(gen_permutations(arr, 2))

# 몇 없는 해쉬테이블 사용 코드
# 대부분 Counter를 이용한 풀이를 함.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        # build a hashmap and save count of each char from the string s
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1

        # iterate over t string and reduce count if the char found in hashmap
        for c in t:
            if c in hashmap:
                hashmap[c] -= 1
            else:
                return False

        # if the anagram is valid the count of each char in the hashmap is 0
        return all(value == 0 for value in hashmap.values())

'''
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start, end = 0, len(s)-1

        while end > start:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

result = Solution()
print(result.isPalindrome("A man, a plan, a canal: Panama"))
'''
'''
class Solution:
    def twoPointer(self, arr: list[int], target: int) -> int:
        arr_length = len(arr)-1
        left, right = 0, 0
        count = 0

        while arr_length != left:
            # print(left, right)
            # if left == 0 and right == 0:
            #     right += 1
            
            if sum(arr[left:right]) >= target:
                print(left, right)
                left += 1
                count += 1
            if sum(arr[left:right]) < target:
                if right == arr_length:
                    left += 1
                else:
                    right += 1

        return count

test = Solution()
print(test.twoPointer([1,2,3,2,4,5,3,2], 6))
'''

'''
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (right+left) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1

        return -1
'''
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0
        for i in range(1,n+1):
            min = sum([1] * i)
            max = sum([2] * i)
            if max >= n >= min:
                if min == n or max == n or i == n:
                    result += 1
                else:
                    result += i

        return result

test = Solution()
print(test.climbStairs(6))


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_integer = {'I': 1, 'V': 5, 'X': 10,
                         'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for char in range(len(s)): # 0 ~ n
            if char != 0:
                if s[char] == 'V' or s[char] == 'X':
                    if s[char-1] == 'I':
                        result += roman_integer[s[char]]-2
                        continue

                if s[char] == 'L' or s[char] == 'C':
                    if s[char-1] == 'X':
                        result += roman_integer[s[char]]-20
                        continue

                if s[char] == 'D' or s[char] == 'M':
                    if s[char-1] == 'C':
                        result += roman_integer[s[char]]-200
                        continue

            result += roman_integer[s[char]]

        return result


test = Solution()
print(test.romanToInt('MCMXCIV'))

# replace 활용 코드
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace(
            "XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))

# 2개씩 끊어 계산, 해쉬 테이블 또한 가능한 수를 모두 만듦
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        sum = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in roman_num:
                sum += roman_num[s[i:i+2]]
                i += 2
            else:
                sum += roman_num[s[i]]
                i += 1

        return sum
'''
'''
x = int(input())

d = [0] * (x+1)

for i in range(2, x + 1):
    # 이전 값으로부터 1을 더한 값
    # 문제에선 d에 해당됨.
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        # 이전 값으로부터 1을 더한 값과 나누기 2를 한 값을 비교
        # 여기서 나누기 2를 한 값에 더해주는 1은 '현재 수를 2로 한번 나누는 행동'에 대하여 더한 것을 의미함.
        # 결론인 즉, x에서 1을 더해준 값 vs x에서 2로 나눈 값을 비교하여
        # 1에서 시작하여 현재값을 만들 수 있는 최소 연산을 dp table에 저장하는 것으로 진행됨.
        # 그리고 바텀업 방식을 사용하였기 때문에 반복이 지속되며 저장하였던 DP table에 있는 값을 계속 불러들여 사용함.
        # 문제에선 c에 해당됨.
        d[i] = min(d[i], d[i//2] + 1)

    if i % 3 == 0:
        # 마찬가지로 이전 값으로부터 1을 더한 값과 나누기 3을 한 값을 비교.
        # 문제에선 b에 해당됨.
        d[i] = min(d[i], d[i//3] + 1)
    
    if i % 5 == 0:
        # 마찬가지로 이전 값으로부터 1 더한 값과 나누기 5를 한 값을 비교.
        # 문제에선 a에 해당됨.
        d[i] = min(d[i], d[i//5] + 1)
    # 이러한 방식으로 풀이 시 예를 들어 x = 6일 때, 1에서부터 6을 만들 수 있는 최소 연산을 구하는 것이지만
    # 동시에 6에서 1을 만들 수 있는 최소 연산을 구하는 것과 동일하게 됨.
    # 1 -> x 로 통하는 가장 빠른 길의 경로를 저장하는 것과 동일함.

print(d[x], d[:x+1])
'''

# - 처음부터 계산하면 된다. (식량이 제일 많은 창고부터 털어나갈 필요가 없음.)
# - 0번부터 계산하여 짝수 인덱스, 1번부터 계산하여 홀수 인덱스의 창고를 모두 두 개의 변수에 담는다.
# -> 잘못된 가설. 반례 7 1 1 8 1의 경우 7+8을 더한 15가 가장 큼.

# 0 + 2, 0 + 3, 0 + 2 4, 0 + 4
# dp_table = [15, 1, 8, 15, 9]
# 방문을 했는 지 어떻게 알 수 있을까?

# 현재 인덱스 위치를 저장하는 변수 index
# 현재 값을 저장하는 dp_table
# 1. index+1 < current_index 일 때만 비교.
# 2. 

# 이전 최대값의 인덱스와 값을 가지고 있는 배열를 만든다. (ex. [0,7])
# 인접한 인덱스인 경우 더하지 않는다.
# 
'''
n = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    print(d[:n+1])
    d[i] = max(d[i - 1], d[i - 2] + array[i])
    print(d[:n+1])
print(d[n-1])
# 현재 배열 공간 + 2칸 전의 배열 공간의 값보다 이전 배열 공간의 값이 더 크다면 현재 공간도 그 값을 넣겠다.

'''
'''
for _ in range(int(input())):
    n, m = map(int,input().split())
    mine = list(map(int,input().split()))
    
    for i in range(m):
        max = 0
        idx = []
        for j in range(n):
            if max < mine[j][i]:
                max = mine[j][i]
                idx = [j, i]
        if 0 <= idx[0]-1 < n and 0 <= idx[1]+1 < n:
            mine[idx[0-1]][idx[1+1]] += max
        if 0 <= idx[1]+1 < n:
            mine[idx[0]][idx[1+1]] += max
        if 0 <= idx[0]+1 < n and 0 <= idx[1]+1 < n:
            mine[idx[0+1]][idx[1+1]] += max
    print(mine)    
'''

for _ in range(int(input())):
    n, m = map(int,input().split())
    gold_mine = list(map(int,input().split()))
    dp_table = []

    for i in range(n):
        dp_table.append(gold_mine[i*m:(i+1)*m])
    
    max = 0
    idx = (0, 0)

    for i in range(m):
        for j in range(n):
            if max < dp_table[j][i]:
                max = dp_table[j][i]
                idx = (j, i)
        
        if i+1 == m:
            break

        if 0 <= idx[0]-1 < n and 0 <= idx[1]+1 < m:
            dp_table[idx[0]-1][idx[1]+1] += max

        if 0 <= idx[1]+1 < m:
            dp_table[idx[0]][idx[1]+1] += max
        
        if 0 <= idx[0]+1 < n and 0 <= idx[1]+1 < m:
            dp_table[idx[0]+1][idx[1]+1] += max

print(max)