# 50 | 30 24 5 28 45 | 98 52 60
# 5 28 24 45 30 | 60 52 98 | 50

# import sys
# sys.setrecursionlimit(10**6)

# def pre_order(tree):
#     # root = tree[0]

#     if len(tree) <= 1:
#         return tree[0]
    
#     for i in range(1,len(tree)):
#         if tree[0] < tree[i]:
#             return pre_order(tree[1:i]) + pre_order(tree[i:]) + tree[0]
    
#     return tree




# tree = [i for i in int(sys.stdin.readline())]
# pre_order(tree)
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

# def kill(k):
#     for _ in range(k-1):
#         n.append(n.pop(0))

#     result.append(n.pop(0))

# n, k = map(int, input().split())
# n = [*range(1, n+1)]
# result = []

# for _ in range(len(n)):
#     kill(k)

# print('<', end='')
# print(*result, sep = ', ', end = '')
# print('>')

# 환형 큐 구현
class circle_queue:
    def __init__(self,length) -> None:
        self.queue = [0]*length
        self.cnt = 0
        self.front = self.queue[0]
        self.rear = self.queue[0]

    def enqueue(self, num):
        if self.empty is not False:
            self.rear = (self.rear+1) % len(self.queue)
            self.queue[self.rear] = num
            self.cnt +=1
        else:
            return False

    def dequeue(self):
        if self.empty is not False:
            self.front = (self.front+1) % len(self.queue)
            print(self.queue.pop(self.front))
            self.queue.append(0)
            self.cnt -= 1

    def size(self):
        print(self.cnt)

    def empty(self):
        if self.cnt == 0:
            return False
        return True
    
    def display(self):
        if self.cnt == 1:
            return False
        print(f'길이는 : {len(self.queue)}')
        for i in range(self.cnt):
            print(self.queue[i])

cq = circle_queue(int(input()))
for _ in range(int(input())):
    command = input().split()

    if command[0] == 'enqueue':
        cq.enqueue(command[1])

    if command[0] == 'dequeue':
        cq.dequeue()

    if command[0] == 'size':
        cq.size()

    if command[0] == 'empty':
        cq.empty()

    if command[0] == 'display':
        cq.display()