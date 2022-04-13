# import sys

# class stack:
#     def __init__(self) -> None:
#         self.stack = []
#         self.cnt = 0

#     def push(self, num):
#         self.stack.append(num)
#         self.cnt += 1

#     def pop(self):
#         if self.cnt == 0:
#             print(-1)
#         else:
#             print(self.stack.pop())
#             self.cnt -= 1

#     def size(self):
#         print(self.cnt)

#     def top(self):
#         if self.cnt == 0:
#             print(-1)
#         else:
#             print(self.stack[-1])

#     def empty(self):
#         if self.cnt == 0:
#             print(1)
#         else:
#             print(0)


# st = stack()
# for _ in range(int(input())):
#     test_list = sys.stdin.readline().split()

#     if test_list[0] == 'push':
#         st.push(test_list[1])

#     if test_list[0] == 'pop':
#         st.pop()

#     if test_list[0] == 'size':
#         st.size()
    
#     if test_list[0] == 'top':
#         st.top()

#     if test_list[0] == 'empty':
#         st.empty()


# BOJ 1158 요세푸스 문제
# 요세푸스 문제는 다음과 같다. 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# N+1개의 배열인 환형큐 회전하며 출력필요
# from collections import deque

# n, k = map(int, input().split())
# deq = deque([*range(1, n+1)])

# print('<', end = '')
# for _ in range(len(deq)-1):
#     for _ in range(k-1):
#         deq.append(deq.popleft())

#     print(f'{deq.popleft()}, ', end = '')

# print(f'{deq[0]}>')

# 환형 큐 구현
# class circle_queue:
#     def __init__(self,length) -> None:
#         self.queue = [0]*length
#         self.cnt = 0
#         self.front = self.queue[0]
#         self.rear = self.queue[0]

#     def enqueue(self, num):
#         if self.empty is not False:
#             self.rear = (self.rear+1) % len(self.queue)
#             self.queue[self.rear] = num
#             self.cnt +=1
#         else:
#             return False

#     def dequeue(self):
#         if self.empty is not False:
#             self.front = (self.front+1) % len(self.queue)
#             print(self.queue.pop(self.front))
#             self.queue.append(0)
#             self.cnt -= 1

#     def size(self):
#         print(self.cnt)

#     def empty(self):
#         if self.cnt == 0:
#             return False
#         return True
    
#     def display(self):
#         if self.cnt == 1:
#             return False
#         print(f'길이는 : {len(self.queue)}')
#         for i in range(self.cnt):
#             print(self.queue[i])

# cq = circle_queue(int(input()))
# for _ in range(int(input())):
#     command = input().split()

#     if command[0] == 'enqueue':
#         cq.enqueue(command[1])

#     if command[0] == 'dequeue':
#         cq.dequeue()

#     if command[0] == 'size':
#         cq.size()

#     if command[0] == 'empty':
#         cq.empty()

#     if command[0] == 'display':
#         cq.display()


# BOJ 1935 후위 표기식2
# 이 문제 다시 풀어보기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import sys

# N = int(input())
# stack = []
# cnt = 0

# for i in input():
#     if i == '+':
#         stack.append(stack.pop()+stack.pop())
#     elif i == '-':
#         last = stack.pop()
#         stack.append(stack.pop()-last)
#     elif i == '*':
#         stack.append(stack.pop()*stack.pop())
#     elif i == '/':
#         last = stack.pop()
#         stack.append(stack.pop()/last)
#     else:
#         if cnt == N:
#             stack.append(solo)
#         if cnt != N:
#             stack.append(int(sys.stdin.readline()))
#             solo = stack[0]
#             cnt += 1
# print(format(*stack,".2f"))


# BOJ 1966 프린터 큐
# test_cases = int(input())

# for _ in range(test_cases):
#     n,m = list(map(int, input().split( )))
#     imp = list(map(int, input().split( )))
#     idx = list(range(len(imp)))
#     idx[m] = 'target'

#     # 순서
#     order = 0
    
#     while True:
#         # 첫번째 if: imp의 첫번째 값 = 최댓값?
#         if imp[0]==max(imp):
#             order += 1
                        
#             # 두번째 if: idx의 첫 번째 값 = "target"?
#             if idx[0]=='target':
#                 print(order)
#                 break
#             else:
#                 imp.pop(0)
#                 idx.pop(0)

#         else:
#             imp.append(imp.pop(0))
#             idx.append(idx.pop(0))   

    # 필요조건
    # 1. 내가 찾으려는 수보다 높은 수가 있다면 그 수가 우선적으로 출력되어야 한다.
    # 2. 만일 나와 동일하거나 같은 수가 있다면 재카운트 시작 1 1 9 1 1 1 의 경우 1 2 순서로 가다가 9를 만나 1로 초기화되고 1 1 1 카운트 내 차례인 1까지




# BOJ 13335 트럭
# n = 트럭의 수
# w = 다리의 길이
# L = 다리의 최대하중
# from collections import deque

# n, w, L = map(int,input().split())
# queue = deque(map(int,input().split()))
# result = 0
# cnt = 0
# start_truck = []

# while True:
#     if L > queue[0]:
#         start_truck.append(queue.popleft())          # 7

#         if len(queue) == 0:
#             print(result + w + len(start_truck))
#             break

#         if sum(start_truck) + queue[0] > L:         # 7 + 4
#             if len(start_truck) > 1:                # truck의 길이가 2 이상이면 length랑 2를 더해준다
#                 result += len(start_truck) + w - 1
#             else:
#                 result += w
#             start_truck = []

# from collections import deque

# n, w, L = map(int,input().split())
# queue = deque(map(int,input().split()))
# result = 0
# cnt = 0
# start_truck = 0

# while True:
#     if L > queue[0]:
#         start_truck += queue.popleft()
#         cnt += 1   
#         n -= 1          

#         if n == 0:
#             print(result + w + cnt)
#             break

#         if start_truck + queue[0] > L:
#             if n > 1:             
#                 result += cnt + w
#             else:
#                 result += w
#             start_truck = 0
#             cnt = 0


# n, w, l = map(int, input().split())
# trucks = list(map(int, input().split()))
 
# bridge = [0] * w 
# weight, time = 0, 0
 
# while True:
#     out = bridge.pop(0)
#     weight -= out
 
#     if trucks: 
#         if weight + trucks[0] <= l:
#             bridge.append(trucks[0])
#             weight += trucks.pop(0)
#         else:
#             bridge.append(0)
#     time += 1

#     if not bridge:
#         break    
# print(time)


# N = int(input())
# result = 1
# bee = 1

# while True:
#     if bee >= N:
#         print(result)
#         break
#     bee += result * 6
#     result += 1


###################################################################### 2022. 04. 13 ################################################################################
# X = int(input())

# line = 0
# max_num = 0

# while X > max_num:
#     line += 1
#     max_num += line

# gap = max_num - X

# if line % 2 == 0:
#     top = line - gap
#     bottom = gap + 1
# else:
#     top = gap + 1
#     bottom = line - gap

# print(f'{top}/{bottom}')


# A, B, V = map(int,input().split())
# result = 0

# day_up = A - B

# if (V - A) % day_up != 0:
#     result = (V - A) // day_up + 2
# else:
#     result = (V - A) // day_up + 1

# print(result)


# for _ in range(int(input())):
#     H, W, N = map(int,input().split())

#     if N % H != 0:
#         xx = N // H + 1
#         yy = N % H
#     else:
#         xx = N // H
#         yy = H

#     xx = str(xx)
#     yy = str(yy)

#     if len(xx) == 1:
#         xx = '0' + xx

#     print(yy + xx)


####################################################################################################################################################################
