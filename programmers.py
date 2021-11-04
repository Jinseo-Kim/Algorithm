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

from collections import Counter

word = Counter(input().upper()).most_common()
if word[0][1] == word[1][1]:
    print("?")
else:
    print(word[0][0])
