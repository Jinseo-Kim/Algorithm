# 입력의 첫 줄에는 테스트 케이스의 수 C가 주어진다.
# 테스트 케이스의 첫 줄에는 학생의 수 n과 친구 쌍의 수 m이 주어진다.
# 그 다음 줄에 m개의 정수 싸응로 서로 친구인 두 학생의 번호가 주어진다.
# 번호는 모두 0부터 n-1 사이의 정수이고, 같은 쌍은 입력에 두번 주어지지 않는다.
# 학생들의 수는 짝수이다.
# 예제 입력
# 3
# 2 1
# 0 1
# 4 6
# 0 1 1 2 2 3 3 0 0 2 1 3
# 6 10
# 0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5
'''
for _ in range(int(input())):
    n, m = map(int,input().split())
    best_friends = list(map(int,input().split()))
    result = 0

    for fixed in range(0,len(best_friends),2):
        possible_combi = [True for _ in range(n)]
        possible_combi[best_friends[fixed]] = False
        possible_combi[best_friends[fixed+1]] = False

        for plus in range(0,len(best_friends),2):
            print(best_friends[plus], best_friends[plus+1], plus)
            if possible_combi[best_friends[plus]] == True:
                if possible_combi[best_friends[plus+1]] == True:
                    possible_combi[best_friends[plus]] = False
                    possible_combi[best_friends[plus+12]] = False

        if True not in possible_combi:
            result += 1
    
    print(result)
'''

import sys
input = sys.stdin.readline


def DFS(startI, remainingFriend):
    if not remainingFriend:
        return 1

    possibleCase = 0

    for i in range(startI, n):
        if not visit[i]:
            for j in range(i + 1, n):
                if not visit[j] and isFriend[i][j]:
                    visit[i] = visit[j] = True
                    possibleCase += DFS(i, remainingFriend - 2)
                    visit[i] = visit[j] = False

    return possibleCase


C = int(input())

for _ in range(C):
    n, m = map(int, input().split())
    visit = [False] * n
    isFriend = [[False] * n for _ in range(n)]
    friendsList = list(map(int, input().split()))

    for i in range(0, len(friendsList), 2):
        isFriend[friendsList[i]][friendsList[i + 1]] = True
        isFriend[friendsList[i + 1]][friendsList[i]] = True

    print(DFS(0, n))
