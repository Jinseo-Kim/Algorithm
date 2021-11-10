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

class stack():
    def push():
        pass

    def pop():
        pass

    def size():
        pass

    def empty():
        pass

    def top():
        pass


for _ in range(int(input())):
    command = list(map(str, input().split()))
    print(command)
