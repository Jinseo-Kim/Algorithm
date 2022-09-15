from collections import deque


def bfs(m, n, cabbage_patch):
    queue = deque()
    switch = 1
    while switch:
        pass

for _ in range(input()):
    m, n, k = map(int,input().split())
    cabbage_patch = [[0]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int,input().split())
        cabbage_patch[y][x] = 1
    move_x, move_y = [-1,1,0,0], [0,0,-1,1]