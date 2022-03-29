def solution(n, computers, result = 0):
    invited = [False for i in range(n)]

    for com in range(n):
        if invited[com] == False:
            dfs(n, computers, invited, com)
            result += 1

    return result

def dfs(n, computers, invited, com):
    invited[com] = True
    for i in range(n):
        if com != i and computers[com][i] == 1:
            if invited[i] is False:
                dfs(n, computers, invited, i)

print(solution(3, [[1,1,0],[1,1,1],[0,1,1]]))