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



###################################################################### 2022. 04. 14 ################################################################################
# 이 문제는 거듭 연산을 주로 다룬 문제이다.
# 0층 1 2 3 1층 1 3 6 2층 1 4 10 이렇게 층별로 아래층의 수만큼 더해 현재 층의 인원 수를 파악하는 문제였고 k층 n호실의 경우, k-1층 n호실까지의 값을 더하면 현재 호실의 값이 나왔다.

# 문제의 풀이는 간단했지만 조금 헤맸다.
# 첫째로 n개의 배열을 만들어 수를 거듭 더해주는 방법을 기본으로 하여 코드를 시작했고
# 0층부터 k층까지 모든 층을 각각 들러 n 길이의 배열에 각각 값을 계속 더해주었다.
# 둘째로 배열의 값을 더해주는 방식은 살짝의 계산이 필요하다.
# 먼저 1호실의 경우 값이 모두 일률적으로 1로 동일하다. 이 말인 즉, 1호실의 경우는 반복할 필요없이 건너 뛰면 되기에 358번째 줄의 코드에서 range()의 범위를 1~n으로 설정했다.
# 그리고 n개의 배열 중 1~n번째까지의 값은 각각 현재 값에 -1번째 인덱스에 해당하는 값을 더해주었다.
# 이렇게 계산하게 되면 한번 반복을 거칠때마다 결국 다음층의 값이 자연스레 배열에 덧씌워지며, 최종적으로 값이 모두 산출된다.
# 여기서 하나를 더 짚고 넘어가자면 k번 반복이고 이 문제는 0층이 있다. 그렇다면 k번 반복했을 때 값이 0+k층의 값이 산출되고 결과로 이어지는 것이다.
'''
for _ in range(int(input())):
    k = int(input())
    n = int(input())

    result = [i for i in range(1,n+1)]

    for _ in range(k):
        for j in range(1, n):
            result[j] += result[j-1]

    print(result[n-1])
'''


# 이 문제는 주어진 값 N에 대한 5kg, 3kg 설탕의 배분 문제이며 수학 + 그리디 알고리즘 문제이다.
# 그리디 알고리즘 간략 서술 : Greedy(탐욕법)을 뜻하며, 주어진 선택지 중 가장 좋은 선택지를 '그 때마다' 고르는 것이다. 최종 결과는 보지않고 현재 주어진 선택지에서 최선의 결과를 선택한다.
# 그리디 알고리즘의 기본이 좀 더 들어갔기에 5kg 설탕을 우선 선택하는 것으로 알고리즘을 구축했다.

# 첫째로 주어진 값 N에 대한 5kg의 몫을 저장하는 변수와 5kg로 나눈 나머지의 설탕을 저장하는 변수를 2개 생성하였다.
# 해당 방법으로 작성한 이유는 최대한의 이득을 보기 위한 5kg의 몫을 구하고 남은 설탕을 3kg의 무게로 구성하려고 했을 때, 불가하다면 5kg를 나머지에 더해
# 3kg의 이득을 구축하기 위함이었다. 요약하자면 5kg 최대한의 몫 -> 3kg 최대한의 몫 -> 3kg로 구성 불가 -> 5kg 몫 - 1 & 남은 설탕 + 5 -> 3kg 최대한의 몫 -> 반복
'''
N = int(input())

five_kg = N // 5
remaining_sugar = N % 5

while True:
    if remaining_sugar % 3 > 0:
        if five_kg <= 0:
            print(-1)
            break
        remaining_sugar += 5
        five_kg -= 1
    else:
        five_kg += (remaining_sugar // 3)
        print(five_kg)
        break
'''


# N = int(input())
# prime_nums = list(map(int,input().split()))
# result = N

# for num in prime_nums:
#     for i in range(2,1001):
#         if num == 1:
#             result -= 1
#             break
#         if num % i == 0 and num != i:
#             result -= 1
#             break

# print(result)


###################################################################### 2022. 04. 15 ################################################################################
# 이 문제는 소수 판별에 대한 문제이다. 주어진 M과 N 사이의 수에서 소수를 판별해내는 알고리즘을 구축하는데 목적이 있다.
# 소수 판별 알고리즘은 크게 3가지로 나뉘며, 2~n까지의 값을 모두 나눠보는 방법과 n의 루트값을 찾아 해당 값을 기준으로 좌측의 수로 나누는 방법.
# 에라토스테네스의 체라는 방법이 있다. 이 풀이에서는 루트값을 찾아 값만큼의 반복을 하며, 소수를 찾는 방법을 사용하였다.

# 첫째로 가장 먼저 M~N만큼의 길이를 가진 배열을 생성해주었다.
# 이후 배열 내 값과 인덱스를 하나씩 넘겨 받으며 1차적으로 반복을 진행하였고, 2차적으로 2 ~ 넘겨받은 값의 루트값 만큼 반복하였다.
# 이때 루트값도 포함시켜야하기 때문에 1을 더한만큼 반복이 진행되었고, 나머지가 0으로 나왔을 때에 해당 배열[인덱스]에 해당하는 값은 0으로 변경해주었다.

# 둘째로 넘겨받은 값이 1일 때의 처리를 하지 않아 값이 1일 때는 1을 0으로 다시 변경해주었고,
# 최종적으로 result(결과값) 변수에 해당 값을 더해주었다.

# 다만 아쉬웠던 점은 원하는 결과값이 상수라고 하여 0으로 만들고 이를 다 더했다는 점이다.
# 0으로 값을 변경함으로써 반복의 효율은 조금 증가하였지만 코드의 난잡함이 더해졌고, Bool타입 연산자의 활용을 제대로 하지 않아
# 다른 사람의 풀이를 보았을 때 bool타입의 활용은 꽤 신기하고 유용하게 다가왔다. 분명 현재 코드에서도 bool타입의 활용은 코드의 편린에 도움을 줄 것이다.

# 결과적으로 보면 단순 상수로 마무리 지으려했던 점은 코드의 가독성에 아쉬움을.
# 단순하게 생각한 풀이를 코드로 옮김은 더 나은 풀이를 도출해내지 못한 것이 아쉬운 점이다.
'''
import math

M = int(input())
N = int(input())
result = 0
min_num = 0

nums = [i for i in range(M, N+1)]

for idx, num in enumerate(nums):
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            nums[idx] = 0

    if num == 1:
        nums[idx] = 0

    if min_num == 0:
        min_num = nums[idx]

    result += nums[idx]

if result == 0:
    print(-1)
else:
    print(result)
    print(min_num)
'''

# 위의 문제를 동일하게 푼 타인의 코드이다. 더 효율이 좋고 어느정도 파이썬을 읽을 줄 안다면 쉽게 이해할 수 있어 가져왔다.
# 이 풀이의 중점은 문제에서 주어진 최대 값의 배열을 미리 생성해두었다는 것이다.
# 소수 판별의 경우, 특히 에라토스테네스의 체의 경우에는 메모리를 활용해 시간 효율성을 증대하는데 의의가 있다.
# 코딩 테스트의 경우에도 대부분 그러하지만 하드웨어의 기술이 비약적으로 발전함에 따라 메모리 관리의 중요도보다 시간 단축의 중요도가 더욱 높아졌다.
# 그렇기에 대개 불필요한 메모리를 사용하는 것은 지양하지만 필요 메모리를 적당한 수준으로 활용해 시간을 단축시키는 건 여러 프로그램에서 많이 쓰이고 있다.
# 이 코드는 그 점을 최대한 활용했다.

# 에라토스테네스의 체는 최소값 2를 시작으로 배수값을 모두 지워가며 설정한 최대값의 한계치에 다다르면 처음으로 돌아가 다음 최소값(소수)을 시작으로해 반복하며 지워가는 특징이 있다.
# 이러한 방법을 사용한 것이 이 코드이며, 원래의 에라토스테네스의 체에서 약수의 특성을 더해 반복의 효율을 높였다.

# 첫째로 최대 값의 배열을 생성해 0번째 인덱스와 1번째 인덱스의 값을 False타입으로 지정해주었다.
# 그 다음 최대값(10000)의 루트값인 100을 지정해 약수의 특성으로 반복의 회수를 1/2로 줄였고, 다음 조건문에서 해당 인덱스의 값이 True라면 실행하도록 했다.
# 둘째로 조건문이 True일 때, 다음 반복문에서 최대의 배열을 현재값 * 2의 시점부터 현재값만큼 이동하며 False로 처리한다.
# 셋째로 이렇게 나온 최대의 배열에서 필요한 만큼의 배열을 결과값의 배열로 분리해내었는데 리스트 컴프리헨션의 조건문으로 해당하는 배열의 값이
# True일 경우에만 분리해 오로지 소수 & True인 결과값만을 담긴 배열로 만들어내었다.
# 이후 출력은 크게 다른 게 없이 출력하지만 이 코드에서는 if문의 삼항 연산자를 사용해 출력하였다. 

# 다만 삼항 연산자는 꼭 필요한 때에만 쓰자.
# 나만이 일을 하는 것은 아니다. 동일 효율성에 가독성을 높인 코딩 방식을 굳이 배제할 필요는 없다.
'''
arr = [False, False] + [True] * 9999
for i in range(2, 101):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

m = int(input())
n = int(input())
nums = [i for i in range(m, n+1) if arr[i]]
print(sum(nums)if len(nums) else -1)
print(min(nums) if len(nums) else '')
'''

# 해당 방법을 통한 소인수분해는 분명히 단순하고 쉬운 방법의 계산이다.
# 하지만 백준을 통해 이 알고리즘의 계산속도를 측정해보았을 때 약 1.5초 정도의 시간이 소요되었다.
# 이만큼의 시간이 소요된 이유는 분명히 while문을 통해 처음부터 끝까지 돌았기 때문이라 생각한다. 이를 계산하기 위해선 좀 더 반복의 횟수를 줄일 필요가 있다.
'''
n = int(input())
divide = 2

while n > 1:
    if n % divide == 0:
        n = n // divide
        print(divide)
    else:
        divide += 1
'''

# 아래의 코드는 위의 코드의 단점을 해결한 코드이다.
# 위의 코드가 O(n)의 시간복잡도를 나타냈다고 하였을 때 아래 코드는 O(n/2) 만큼의 시간복잡도를 갖고 있다.
# 소인수분해에서 시간을 줄일 수 있는 중점은 약수의 존재였다.
# 여러 수에는 약수가 존재하고 소인수분해는 최소의 약수로 나누었을 때 나오는 최대한의 횟수를 구하는 것이기 때문에 최소의 약수를 찾아 나누어주면 시간을 절약할 수 있다.
# 예시를 들자면 16에는 1 2 4 8 16이 있고, 이 수들은 4를 기준으로 대칭되는 수를 곱했을 때 처음의 수(16)이 나오게된다.
# 그 말인 즉, 4를 기준으로 왼쪽의 수들은 약수 중 최소약수를 뜻하고 이 수들을 기준 삼아 최대한의 횟수로 나누게 되면 원하는 해를 얻어낼 수 있다.
'''
n = int(input())
i = 2
r = int(n ** 0.5)       # 이 부분은 math.sqrt()부분과 동일하게 해당 수를 0.5로 제곱하여 루트값를 도출한 코드이다.

while i <= r:        # 461 ~ 464는 위의 코드와 유사하며 동일하게 동작한다. 다만 460 부분의 코드에서 회전 수를 1/2배 감소시켜 더 빠른 결과를 도출해내었다.
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)
'''

# 그래도 최근 3일간 문제를 풀며 결과 도출에 있어 속도가 조금은 상승한 것 같다. 이전에 풀지 못했던 벌집 문제도 설탕 배분 문제도 어떻게 보면 간단했었던 문제들이지만
# 문제를 푸는 데에 있어서는 꾸준한 생각과 근성. 풀리지 않는다면 적당한 타협을 통해 여러 풀이를 접하고 방법을 터득하는 것이 좋다는 생각이 들었다.


# 이번 풀이는 꽤 괜찮았다. 소수 판별 알고리즘을 검색하며 알게 된 에라토스테네스의 체를 위의 소수를 풀며 좋은 풀이로 한번 접했고,
# 이를 실제로 문제에 적용해보았으니 좋은 경험이 되었다고 생각한다.
# 하지만 소수 판별. 특히 에라토스테네스의 체 같은 경우, 주기적으로 한번씩 코드를 보거나 다시 풀어보는 게 중요하다고 생각한다.
# 한번 정도의 좋은 경험은 실력이 될 수 없다. 여러번 풀이를 만들어내 외우든 익히든 실제 경험치로 남겨야 의미가 있다.
'''
m, n = map(int,input().split())
nums = [False if i < 2 else i for i in range(n+1)]
divide = 2

while n > 2:
    if divide == n:
        break

    if nums[divide]:
        for i in range(2 * divide, n+1, divide):
            nums[i] = False
    divide += 1

for num in nums:
    if n >= num >= m:
        print(num)
'''

# 풀긴 했지만 너무 느리다...왤까?
'''
import sys

nums = [False, False] + [True] * 246950

while True:
    n = int(sys.stdin.readline())
    max_num = 2 * n
    result = 0

    if n == 0:
        break

    for i in range(2, int(max_num ** 0.5)+1):
        if nums[i]:
            for j in range(i * 2, max_num+1, i):
                nums[j] = False

    for num in nums:
        if max_num >= num > n:
            result += 1
    
    print(result)
'''

'''
d = [True] * (2 * 123456)
d[0], d[1] = False, False
for i in range(2, 2 * 123456):
    for j in range(2 * i, 2 * 123456, i):
        d[j] = False
sosu = [i for i in range(2 * 123456) if d[i] == True]

k = True
while k:
    n = int(input())
    if n == 0:
        k = False
        break
    ans = 0
    for i in sosu:
        if n < i <= 2*n:
            ans += 1
    print(ans)
'''


###################################################################### 2022. 04. 18 ################################################################################
'''
prime_num = list(range(10001))
prime_num[0], prime_num[1] = False, False

while True:
    for i in range(2, int(10000 ** 0.5)+1):
        if prime_num[i]:
            for j in range(i * 2, 10001, i):
                prime_num[j] = False
    break

for _ in range(int(input())):
    n = int(input())
    left = n // 2
    right = left

    for i in range(left):
        if prime_num[left] and prime_num[right]:
            print(f'{prime_num[left]} {prime_num[right]}')
            break
        left -= 1
        right += 1
'''

###################################################################### 2022. 04. 19 ################################################################################
'''
x, y, w, h = map(int,input().split())
result = 0

if x > y:
    result = y
else:
    result = x

if result >= w - x:
    result = w - x
if result >= h - y:
    result = h - y

print(result)
'''


'''
x_list, y_list = [], []
for _ in range(3):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

result = [0, 0]

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        result[0] = x_list[i]
    if y_list.count(y_list[i]) == 1:
        result[-1] = y_list[i]

print(*result)
'''


###################################################################### 2022. 04. 20 ################################################################################
'''
while True:
    pytha_nums = sorted(list(map(int, input().split())))

    if sum(pytha_nums) == 0:
        break
    
    if (pytha_nums[0] ** 2) + (pytha_nums[1] ** 2) == pytha_nums[2] ** 2:
        print('right')
    else:
        print('wrong')


r = int(input())

print(f'{r * r * 3.141592653628118:6f}')
print(f'{r * r * 2:6f}')
'''

###################################################################### 2022. 04. 21 ################################################################################


###################################################################### 2022. 04. 26 ################################################################################
'''
def fibonacci(n, cnt = 1, prev = 0, current = 1):
    if n == cnt:
        return current

    cnt += 1
    return fibonacci(n, cnt, current, current + prev)
    

n = int(input())
if n == 0 or n == 1:
    print(n)
else:
    print(fibonacci(n))
'''
###################################################################### 2022. 04. 27 ################################################################################
#### 다ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ시ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ풀어ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓ보ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ기ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ#######
'''
def draw_star(n):
    global Map

    if n == 3:
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return

    a = n//3
    draw_star(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]  # 핵심 아이디어


N = int(input())

# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''


###################################################################### 2022. 04. 28 ################################################################################
# 하노이의 탑은 나중에 풀어보자.... 더 쉬운 문제로 재귀를 익힌 뒤에
'''
def hanoi(first, second, third, cnt, result, n):
    if n-1 in first:
        block = first.pop()
        if block == n-1:
            if second[-1] > block:
                second.append(block)
                result.append([1, 2])
                cnt += 1

n = int(input())
first = [i for i in range(n,0,-1)]
second, third = [0], [0]
result = []
cnt = 0

if n % 2 == 1:
    third[0] = first.pop()
    result.append([1, 3])
else:
    second[0] = first.pop()
    result.append([1, 2])
cnt += 1

hanoi(first, second, third, cnt, result, n)
'''

'''
def plus_num(n, start_num):
    global result
    if start_num >= n:
        if start_num == n:
            result += 1
        return
    if start_num < n:
        plus_num(n, start_num + 1)
    if start_num < n:
        plus_num(n, start_num + 2)
    if start_num < n:
        plus_num(n, start_num + 3)

    return result

for _ in range(int(input())):
    n = int(input())
    result = 0
    for i in range(1,4):
        plus_num(n, i)
    print(result)
'''

'''
N = int(input())
arr = [1, 2, 4]
for _ in range(4, 11):
    arr.append(sum(arr[-3:]))
for _ in range(N):
    T = int(input())
    print(arr[T-1])
'''
def slice_paper(confetti, result, n, m = 1):
    for i in range(m):
        for j in range(n):
            if 1 in confetti[j][n*i:n*(i+1)]:
                if 0 in confetti[j][n*i:n*(i+1)]:
                    slice_paper(confetti, result, n // 2, m * 2)
                else:
                    result[0] += 1
            else:
                result[1] += 1
    return result


n = int(input())
confetti = [list(map(int,input().split())) for i in range(n)]
result = [0, 0]     # 첫번째 인덱스 = white, 두번째 인덱스 = blue
print(slice_paper(confetti, result, n))
print(result)