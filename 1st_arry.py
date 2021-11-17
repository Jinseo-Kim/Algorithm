# 최대값
# numbers = [int(input()) for _ in range(9)]
#
# print(max(numbers))
# print(numbers.index(max(numbers)) + 1)

#2577 숫자의 개수
# numbers = [int(input()) for _ in range(3)]
# sum = 1
# for i in numbers:
#     sum *= i
# sum = str(sum)
# num, count_ = 0, []
# for j in range(len(sum)):
#     count_.append(sum[num])
#     num += 1
# for i in range(10):
#     print(count_.count(str(i)))

# 2577 조흔 답안
# a = int(input())
# b = int(input())
# c = int(input())
# # 여기서 map(함수, iterable 반복가능객체)
# d = list(map(int, (str(a * b * c))))
# print(d)
# for i in range(10):
#     print(d.count(i))

#3052 나머지(깔쌈코드)
# value = set([int(input())%42 for _ in range(10)])
# print(len(value))

#1546 평균(깔쌈코드)
# repeat = int(input())
# score = sorted(list(map(int, input().split())),reverse=True)
# result = sum([score[i]/score[0]*100 for i,j in enumerate(score)])
# print(result/len(score))

#1152 단어의 개수
# print(len(input().split(' ')))

#2908 상수
# a, b = input().split()
# print(max(int(a[::-1]), int(b[::-1])))

#5622 다이얼
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = input()
# ret = 0
# for j in range(len(a)):
#     for i in dial:
#         if a[j] in i:
#             ret += dial.index(i)+3
# print(ret)

#2941 크로아티아 알파벳
# cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# n = input()
# value, cnt = 0, 0
# for i in range(1,len(n)+1):
#     for j in cro:
#         if j in n[value:i]:
#             cnt += 1-len(j)
#             value = i
#
# if cnt == 0:
#     print(len(n))
# else:
#     print(len(n)+cnt)

#2941 크로아티아 알파벳 좋은 코드
# w=input();print(len(w)-sum(w.count(a)for a in['=','-','lj','nj','dz=']))

#1316번 그룹 단어 체커
# import sys
#
# n = int(input())
# cnt = 0
# for _ in range(n):
#     word = sys.stdin.readline().rstrip()
#     for i,j in enumerate(word):
#         if word.count(j) > 1 and word[i+1:].find(j) > 0:
#             break
#         elif i == len(word)-1:
#             cnt += 1
# print(cnt)
#
# result = 0
# for i in range(int(input())):
#     word = input()
#     print(sorted(word))
#     if list(word) == sorted(word):
#         result += 1
# print(result)


# n, k = map(int, input().split())
# people, result = list(range(1,n+1)), []
# a = k-1
#
# for _ in range(1, n+1):
#     result.append(people.pop(k-1))
#
#     if len(people) < k+a:
#         k = (k+a)-len(people)
#     elif len(people) > 1:
#         k = k+a
#     print(k)
#     if k > len(people):
#         k = k%len(people)
#
# result = ', '.join(str(_)for _ in result)
# print(f'<{result}>')

# 9012번 괄호
# import sys
#
# i = int(input())
#
# for _ in range(i):
#     a = 0
#     vps = sys.stdin.readline()
#
#     if vps.count("(") == vps.count(")"):
#         for i in range(vps.count(")")):
#             a = vps.index(")",a)+1
#             if vps.count("(",0,a) < vps.count(")",0,a):
#                 print("NO")
#                 break
#
#             elif i == vps.count(")")-1:
#                 print("YES")
#     else:
#         print("NO")

# 후위 표기법2
# import sys
#
# N = int(input())
# form = input()
#
# get, stack = 0, []
#
# for i in range(len(form)):
#     if form[i].isalpha() == True:
#         num = int(sys.stdin.readline())
#         stack.append(num)
#
#     if form[i] == "+":
#         get = stack.pop()
#         stack.append(stack.pop() + get)
#
#     elif form[i] == "-":
#         get = stack.pop()
#         stack.append(stack.pop() - get)
#
#     elif form[i] == "*":
#         get = stack.pop()
#         stack.append(stack.pop() * get)
#
#     elif form[i] == "/":
#         get = stack.pop()
#         stack.append(stack.pop() / get)
#
# print(round(stack.pop(),2))

# 괄호 Renew
# import sys
#
# T = int(input())
# stack = []
# _sum = []
#
# for _ in range(T):
#     vps = sys.stdin.readline()
#     for i in range(len(vps)):
#         stack.append(vps[i])
#         if vps[i] == ")":
#             stack.pop()
#             stack.pop()
#     if len(_sum) == len(stack):
#         print("YES")
#     else:
#         print("NO")

# import sys
# import math

# def plus_num(heap):
#     index = len(heap)-1
#     while  index > 0 and heap[index] > heap[(index-1)//2]:
#         heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
#         index = (index-1)//2
#     return heap

# def chg(heap):
#     heap_len = len(heap)
#     if heap_len > 1:
#         origin = 0
#         heap[0] = heap.pop()
#         heap_len-=1
#         while True:
#             right = origin*2+2
#             left = origin*2+1
#             if heap_len <= left:
#                 break

#             next_ = origin
#             if heap[left] > heap[origin]:
#                 next_ = left
            
#             if heap_len > right:
#                 if heap[next_] < heap[right]:
#                     next_ = right
#             if next_ == origin:
#                 break

#             heap[next_], heap[origin] = heap[origin], heap[next_]
#             origin = next_

#     else:
#         heap.pop()

#     return heap




# N = int(input())
# heap = []

# for _ in range(N):
#     num = int(sys.stdin.readline())
#     if num == 0:
#         if len(heap) > 0:
#             print(heap[0])
#             heap = chg(heap)
#         else:
#             print(0)

#     else:
#         heap.append(num)
#         plus_num(heap)




# 상근이는 카드 n(4 ≤ n ≤ 10)장을 바닥에 나란히 놓고 놀고있다. 각 카드에는 1이상 99이하의 정수가 적혀져 있다.
# 상근이는 이 카드 중에서 k(2 ≤ k ≤ 4)장을 선택하고, 가로로 나란히 정수를 만들기로 했다. 상근이가 만들 수 있는 정수는 모두 몇 가지일까?
# n = int(input())
# k = int(input())

# if 4 <= n <= 10 and 2 <= k <= 4:
#     card_pack = list(map(lambda x:str(x) if x<=99 else 0,[int(input()) for _ in range(n)]))
# if 0 not in card_pack:
#     new_list = []
#     for i in range(n):
#         for j in range(n*(k-1)):
#             if i == j:
#                 continue
#             else:
#                 new_list.append(card_pack[i]+card_pack[j])
# print(f'list개수 : {len(new_list)}\n리스트 인자 : {new_list}')
# print(len(set(new_list)))
