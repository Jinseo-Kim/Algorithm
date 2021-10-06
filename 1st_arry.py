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

import sys
def change(heap):
    two_to = len([i for i in range(len(heap)) if 2**i <= len(heap)])
    origin, chg_save = 0, 0
    for _ in range(two_to-1):
        if heap[origin*2+1] > heap[origin]:
            heap.insert(origin, heap.pop(origin*2+1))
            chg_save = heap.pop(origin+1)
            heap.insert(origin*2+1, chg_save)

            origin = origin*2+1
        elif heap[origin*2+2] > heap[origin]:
            heap.insert(origin, heap.pop(origin*2+2))
            chg_save = heap.pop(origin+2)
            heap.insert(origin*2+2, chg_save)

            origin = origin*2+2
        else:
            break
    return heap

N = int(input())
heap, save = [], 0

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0 and len(heap) == 0:
        print(0)
    elif num == 0 and len(heap) >= 1:
        print(heap.pop(0))
        if len(heap) >= 2:
            print(heap)
            heap = change(heap)
    else:
        heap.append(num)
        if len(heap) > 1:
            index, change = len(heap)-1, len(heap)-1
            two_to = len([i for i in range(len(heap)) if 2**i <= len(heap)])
            for _ in range(two_to-1):
                if index%2 == 1:
                    index = (index-1)//2
                elif index%2 == 0:
                    index = (index-2)//2
                else:
                    index = 0

                if heap[index] < heap[change]:
                    save = heap.pop(change)
                    heap.insert(index,save)
                    heap.insert(change,heap.pop(index+1))

                    change = index
                else:
                    break
            print(heap)
