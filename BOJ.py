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


# BOJ 9012 괄호
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.


# 1. T번 반복하며 입력받기
# 2. 각 횟수당 YES, NO 형태로 출력하기
# - 조건 : 시작하는 문자열이 )이면 안되며, 끝나는 문자열이 (이면 안된다.
#         괄호의 개수는 짝수여야한다.
#         스택을 통해 구현하며 ( 괄호를 더하고 )을 만나면 하나씩 pop한다. 이후 마지막까지 돌았으나 잔여 스택의 개수가 0이면 YES
# import sys

# for _ in range(int(input())):
#     stack = []
#     vps = sys.stdin.readline().strip()

#     if len(vps) % 2 == 1:
#         print('NO')

#     elif vps[0] == ')' or vps[-1] == '(':
#         print('NO')

#     else:
#         for i in vps:
#             if i == '(':
#                 stack.append('(')
#             if i == ')':
#                 if len(stack) > 0:
#                     stack.pop()
#                 else:
#                     stack.append('underflow')
#                     break
        
#         if len(stack) > 0:
#             print('NO')
#         else:
#             print('YES')

# BOJ 10799 제로
# 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
# 이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1, 000, 000 사이의 값을 가지며, 정수가 "0" 일 경우에는 
# 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
# import sys

# stack = []
# for _ in range(int(input())):
#     num = int(sys.stdin.readline())
#     if num > 0:
#         stack.append(num)
#     if num == 0:
#         stack.pop()
# print(sum(stack))

# BOJ 10799 쇠막대기
# 여러 개의 쇠막대기를 레이저로 절단하려고 한다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 
# 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다.
# 이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.
# - 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
# - 쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다. 
# 1. ()이 비로소 레이저를 뜻하기 때문에 (을 더해가다가 )을 만나면 그 순간 앞에 있는 막대기의 ( 개수에 따라 절단이 이루어진다.
# 2. () 이후)이 하나 더나온다면 이것은 레이저가 아니라 막대기의 끝을 의미한다. 이때를 구분하는 코드가 들어가야한다.
# 3. 막대기 개수를 세는 게 아니라 절단 횟수를 세었기 때문에 막대기의 끝에는 그게 +1 더해야한다.
# 3. 전체 막대기의 절단 개수를 세고 이걸 변수에 넣는다.

# import sys

# stack = []
# result = 0
# chg = 0
# for i in sys.stdin.readline().strip():
#     if i == '(':
#         stack.append('(')
#         chg = 1
#     if i == ')':
#         if chg == 1:
#             stack.pop()
#             result += len(stack)
#             chg = 0
#         elif chg == 0:
#             stack.pop()
#             result += 1
# print(result)





# BOJ 1935 후위 표기식
# 1. postfix의 횟수만큼 순회
# 2. 각 숫자를 입력받고 영어대문자가 나올 때마다 입력.
# import sys

# N = int(input())
# postfix = list(input())
# stack = []
# cnt = 0

# for i in postfix:
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




# BOJ 11005 진법 변환 2 
# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# N, B = map(int,input().split())
# result = []

# while N != 0:
#     if N % B >= 10:
#         result.append(chr((N % B)+55))
#     else:
#         result.append(str(N % B))
#     N = N//B

# print(*result[::-1], sep = '')




# BOJ 2745 진법 변환
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# N, B = map(str,input().split())
# string = list(N)
# string.reverse()
# result = 0

# for i,j in enumerate(string):
#     if ord(j) >= 65:
#         result += int(B)**i*(ord(j)-55)
#     else:
#         result += int(B)**i*int(j)

# print(result)




# BOJ 1212 8진수 2진수
# 8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.

# num = '0o'+input()
# print(bin(int(num, 8))[2:])




# BOJ 1373 2진수 8진수
# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

# num = '0b'+input()
# print(oct(int(num, 2))[2:])




# BOJ 10988 팰린드롬인지 확인하기
# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.
# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

# string = input()

# if string == string[::-1]:
#     print(1)
# else:
#     print(0)




# BOJ 2588 곱셈
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# first_num = int(input())
# second_num = int(input())
# arr_sec = [int(i) for i in str(second_num)]
# arr_sec.reverse()

# for i in arr_sec:
#     print(first_num * i)

# print(first_num * second_num)




# BOJ 2490 윷놀이
# 우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다.
# 네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 
# 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.
# yut_result = ['E','A','B','C','D']

# for _ in range(3):
#     yut = list(map(str,input().split()))
#     print(yut_result[yut.count('0')])




# BOJ 11650 좌표 정렬하기
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 
# 정렬한 다음 출력하는 프로그램을 작성하시오.
import sys

result = []
for i in range(int(input())):
    result.append(list(map(int,sys.stdin.readline().split())))

result.sort()
print(*result)