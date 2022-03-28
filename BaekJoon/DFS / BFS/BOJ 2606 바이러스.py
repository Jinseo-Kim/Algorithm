from itertools import count

def answer(virus, coms_num):
    virus[1] = True

    for i in range(int(input())):
        start, end = map(int, input().split())

        if virus[start] is True:
            dfs(start, end, virus, coms_num)  #dfs[end] = True

        if virus[start] is False and virus[end] is True:
            virus[start] = True

    return virus.count(True)-1

def dfs(start, end, virus, coms_num):
    pass




coms = int(input())
coms_num = [[i] for i in range(coms+1)]
virus = [0 if i == 0 else False for i in range(coms+1)]

# 1 2
# 3 5
# 2 3
# 1 4
# 8 9