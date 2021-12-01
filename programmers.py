# def solution(L, x):
#     answer = []
#
#     for i,j in enumerate(L):
#         if L.count(x) == 0:
#             answer.append(-1)
#             break
#
#         if j == x:
#             answer.append(i)
#
#     return answer
#
# L = [64, 72, 83, 72, 54]
# x = 49
# print(solution(L,x))


# MAP = [list(map(int, input().split())) for _ in range(int(input()))]
# print(MAP)

# from collections import Counter
#
# word = Counter(input().upper()).most_common()
# if len(word) > 1 and word[0][1] == word[1][1]:
#     print("?")
# else:
#     print(word[0][0])

# def solution(mylist):
#     answer = []
#     for number1, number2 in zip(mylist, mylist[1:]):
#         answer.append(abs(number1 - number2))
#     return answer
#
# if __name__ == '__main__':
#     mylist = [83, 48, 13, 4, 71, 11]
#     print(solution(mylist))


# word = [ord(i)+23 if ord(i)+23 <= 90 else ord(i)-3 for i in list(input())]
# print(''.join(list(map(chr,word))))

# fact = 1
# N = int(input())
# if N == 0:
#     print(1)
# else:
#     for i in range(1,N):
#         fact = fact*(i+1)
#     print(fact)

# value = set(map(lambda x: x if x%2==1 else 0, [int(input()) for _ in range(7)]))
# value.remove(0)
# if len(value) > 0:
#     print(f'{sum(value)}\n{min(value)}')
# else:
#     print(-1)

# for _ in range(int(input())):
#     binary = []
#     n = list(bin(int(input()))[2:])
#     n.reverse()
#
#     for i in range(len(n)):
#         if n[i] == '1':
#             binary.append(i)
#
#     print(*binary)

# from itertools import combinations
# def solution(nums):
#     nums_list = list(map(lambda x: sum(list(x)),combinations(nums,3)))
#     print(nums_list)
#     for i,j in enumerate(nums_list):
#         for k in nums:
#             if j%k == 0 and k != 1:
#                 nums_list[i] = 0
#                 break
#             else:
#                 pass
#
#     nums_list = set(nums_list)
#     nums_list.remove(0)
#     print(len(nums_list))
#
#
#
#
# nums = [1,2,7,6,4]
# solution(nums)

# from itertools import combinations

# class stack():
#     def __init__(self):
#         self.stack_list = []

#     def push(self,num):
#         self.stack_list.append(num)

#     def pop(self):
#         pass

#     def size(self):
#         pass

#     def empty(self):
#         pass

#     def top(self):
#         pass


# for _ in range(int(input())):
#     command = list(map(str, input().split()))
    

# 순열 for문으로 구축해보기 (Combinations편)

# start_num = 5
# result = []

# for i in range(1,start_num+1):
#     for j in range(i+1, start_num):
#         result.append((i,j))

# print(result)

# 순열 for문으로 구축해보기 (Permutations편)

# a = ['A','B','C']
# result = []

# for i in range(len(a)):
#     for j in range(len(a)):
#         if i == j:
#             pass
#         else:
#             result.append((a[i],a[j]))

# print(result)


# Singled linked list (단일 연결 리스트)
class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next
    
def init():    
    global node1
    # 데이터 부분
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # 포인터 부분
    node1.next = node2
    node2.next = node3
    node3.next = node4

def insert(data):
    global node1
    new_node = Node(data)
    new_node.next = node1
    node1 = new_node

def delete(delete_data):
    global node1
    prev_node = node1
    next_node = node1.next
    if delete_data == prev_node.data:
        del prev_node
    
    while next_node:
        if delete_data == next_node.data:
            prev_node.next = next_node.next
            del next_node
            break

        prev_node = next_node
        next_node = next_node.next

def print_list():
    global node1
    prev_node = node1
    while True:
        print(prev_node.data)
        if prev_node.next is None:
            break
        prev_node = prev_node.next

init()
insert(9)
delete(3)
print_list()

