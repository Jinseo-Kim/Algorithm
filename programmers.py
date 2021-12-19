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


# <<<<<<< Updated upstream
# <<<<<<< Updated upstream
# # Singled linked list (단일 연결 리스트)
# class Node:
#     def __init__(self, data, next = None) -> None:
#         self.data = data
#         self.next = next
    
# def init():    
#     global node1
#     # 데이터 부분
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)

#     # 포인터 부분
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4

# def insert(data):
#     global node1
#     new_node = Node(data)
#     new_node.next = node1
#     node1 = new_node

# def delete(delete_data):
#     global node1
#     prev_node = node1
#     next_node = node1.next
#     if delete_data == prev_node.data:
#         del prev_node
    
#     while next_node:
#         if delete_data == next_node.data:
#             prev_node.next = next_node.next
#             del next_node
#             break

#         prev_node = next_node
#         next_node = next_node.next

# def print_list():
#     global node1
#     prev_node = node1
#     while True:
#         print(prev_node.data)
#         if prev_node.next is None:
#             break
#         prev_node = prev_node.next

# init()
# insert(9)
# delete(3)
# print_list()

# import sys
# import os
# import openpyxl
# from openpyxl.drawing.image import Image

# '/Users/jskim2/Downloads/Coverage/coverage/12/pos1/total_coverage.png'.info['dpi']

# import sys

# cnt = 0
# stack = []
# N = int(input())
# post = list(input())

# for i in range(len(post)):
#     if post[i] == '+':
#         n2 = stack.pop()
#         n1 = stack.pop()
#         stack.append(n1+n2)
#     elif post[i] == '-':
#         n2 = stack.pop()
#         n1 = stack.pop()
#         stack.append(n1-n2)
#     elif post[i] == '*':
#         n2 = stack.pop()
#         n1 = stack.pop()
#         stack.append(n1*n2)
#     elif post[i] == '/':
#         n2 = stack.pop()
#         n1 = stack.pop()
#         stack.append(n1/n2)
#     elif N > cnt:
#         cnt += 1
#         stack_num = int(sys.stdin.readline())
#     else:
#         stack.append(stack_num)

# print(stack)
#N = int(input())
#for i in range(1,N):
#    print((' '*(N-i))+'*'*(2*i-1)+(' '*(N-i)), end = '')
#for i in range(N):
#    print((' '*i+('*'*(2*N-2*i-1))+' '*i).rstrip())
#
#number = int(input())
#
#for i in range(1, number):
#    print(' ' * (number - i), end='')
#    print('*' * (2 * i - 1))
#for i in range(number, 0, -1):
#    print(' ' * (number - i), end='')
#    print('*' * (2 * i - 1))


#N = int(input())
#for i in range(N-1):
#    print(' '*i+'*'*(2*N-2*i-1))
#for i in range(N):
#    print(' '*(N-i-1)+'*'*(2*i+1))


# # 단일 연결 리스트 (끝에 삽입, 선택한 노드 뒤 삽입, 선택한 노드 삭제 구현)
# class Node: # 노드의 생성문 
#     def __init__(self,data,next = None):
#         self.data = data #3
#         self.next = next #None

# class main: # 메인 메서드 동작 및 Head / Tail 생성문
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None

#     def end_insert(self,data): # O(1)
#         new_node = Node(data)

#         if self.head is None:  # 값이 비어있다면 실행
#             self.head = new_node 
#             self.tail = new_node
#         else:                  
#             self.tail.next = new_node
#             self.tail = new_node

#     def select_insert(self, data, pick_node): # O(n)
#         new_node = Node(data)
#         search = self.head

#         while self.head is not None:
#             if search.data == pick_node:
#                 new_node.next = search.next
#                 search.next = new_node
#                 break
#             else:
#                 search = search.next


#     def select_remove(self, pick_node): # O(n)
#         prev_node = self.head
#         current_node = self.head.next # 2->3, 3->4, 4->None

#         while self.head is not None:
#             if self.head.data == pick_node:
#                 self.head = None
#                 self.head = self.head.next
#                 break
#             if current_node.data == pick_node:
#                 prev_node.next = current_node.next
#                 break
#             else:
#                 prev_node = current_node
#                 current_node = current_node.next

# def print_node():
#     iterator = linked_list.head
#     while iterator:
#         print(f'{iterator.data}, {iterator.next}')
#         iterator = iterator.next


# if __name__ == '__main__':
#     linked_list = main()
#     linked_list.end_insert(2)
#     linked_list.end_insert(3)
#     linked_list.end_insert(4)
#     print_node()




# # 이중 연결 리스트
# class Node:
#     def __init__(self, data, next = None, prev = None) -> None:
#         self.prev = prev
#         self.data = data
#         self.next = next

# class main:
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None
    
#     def insert(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
    
#     def select_remove(self, pick_node):
#         check_node = self.head

#         while check_node:
#             if self.head.data == pick_node:
#                 self.head = self.head.next
#                 self.head.prev = None
#                 break
            
#             if check_node.data == pick_node: 
#                 if check_node.next is None: # tail.next = None 값이 2개거나 tail일 때
#                     check_node.prev.next = None
#                     self.tail = check_node.prev
#                     break
#                 else:
#                     check_node.prev.next = check_node.next
#                     check_node.next.prev = check_node.prev
#                     check_node.prev = None
#                     check_node.next = None
#                     break
#             else:
#                 check_node = check_node.next


# def print_node():
#     iterator = double.head
#     while iterator:
#         print(f'iterator prev : {iterator.prev}    iterator data : {iterator.data}    iterator next : {iterator.next}')
#         iterator = iterator.next


# if __name__ == '__main__':
#     double = main()
#     double.insert(2)
#     double.insert(3)
#     double.insert(4)
    
#     print_node()

# # 환형 연결 리스트 (끝에 삽입, 선택한 노드 뒤 삽입, 선택한 노드 삭제 구현)
# class Node: # 노드의 생성문 
#     def __init__(self,data,next = None):
#         self.data = data
#         self.next = next 

# class main: # 메인 메서드 동작 및 Head / Tail 생성문
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None

#     def end_insert(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node 
#             self.tail = new_node
#         else:                  
#             self.tail.next = new_node
#             self.tail = new_node
#             self.tail.next = self.head

#     def select_insert(self, data, pick_node):
#         new_node = Node(data)
#         search = self.head

#         while self.head is not None:
#             if self.tail.data == pick_node:
#                 new_node.next = self.tail.next
#                 self.tail.next = new_node
#                 self.tail = new_node
#                 break
#             if search.data == pick_node:
#                 new_node.next = search.next
#                 search.next = new_node
#                 break
#             else:
#                 search = search.next


#     def select_remove(self, pick_node):
#         prev_node = self.head
#         current_node = self.head.next

#         while self.head is not None:
#             if self.head.data == pick_node:
#                 self.head.next = None
#                 self.head = current_node
#                 self.tail.next = self.head
#                 break
#             if current_node.data == pick_node:
#                 prev_node.next = current_node.next
#                 break
#             else:
#                 prev_node = current_node
#                 current_node = current_node.next

# def print_node():
#     iterator = linked_list.head
#     while True:
#         print(f'현재 노드의 객체 : {iterator}\n현재 노드의 데이터 : {iterator.data}\n현재 노드의 포인터 : {iterator.next}\n')
#         iterator = iterator.next
#         if iterator.data == linked_list.head.data:
#             break
#         else:
#             pass


# if __name__ == '__main__':
#     linked_list = main()
#     linked_list.end_insert(2)
#     linked_list.end_insert(3)
#     linked_list.end_insert(4)
#     linked_list.select_remove(2)
    
#     print_node()
##################################### 싱글 링크드 링스트 고쳐라!!!!!!!!! #####################################