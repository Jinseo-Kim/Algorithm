from itertools import count

def answer(virus, coms_num):
    virus[1] = True

    for i in range(int(input())):       # 컴퓨터 쌍의 수만큼 반복
        start, end = map(int, input().split())
        coms_num[start].append(end)
        coms_num[end].append(start)

        if virus[start] is True or virus[end] is True:
            dfs(coms_num, start, virus)

    return virus.count(True)-1

def dfs(coms_num, start, virus):
    for com in coms_num[start]:
        if virus[com] is False:
            virus[com] = True
            dfs(coms_num, com, virus)

    return virus


coms = int(input())
coms_num = [[i] for i in range(coms+1)]     # [[0], [1], [2], [3], [4], [5], [6], [7]]
virus = [0 if i == 0 else False for i in range(coms+1)]     # [0, False, False, False, False, False, False, False]
print(answer(virus, coms_num))


# 1. 바이러스의 start번째가 True인지 확인
# 2. 바이러스의 end번째가 True인지 확인
# 3. dfs 실행 (start, end 값을 각각 보내서 바이러스에 대입할 게 아닌 리스트를 인덱스로 지정해 보내는 게 더 낫지 않을까..)
# 4. start / end에 따라서 엮여있는 쌍에게 True로 이전
# 5. append 이전에 dfs 재귀 (탐색 조건은 각 쌍에 엮여있는 또다른 리스트)
# 1 2
# 4 3
# 5 6
# 3 2
# 4 5