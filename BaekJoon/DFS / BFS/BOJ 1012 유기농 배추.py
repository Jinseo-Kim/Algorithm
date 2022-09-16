from collections import deque


def bfs(m, n, cabbage_patch, cabbages, count = 0):
    queue = deque()
    move_x, move_y = [-1, 1, 0, 0], [0, 0, -1, 1]

    for cabbage in range(len(cabbages)):
        queue.append(cabbages[cabbage])
        cab_y, cab_x = queue[0]

        if cabbage_patch[cab_y][cab_x] == 1:
            cabbage_patch[cab_y][cab_x] = 2
            count += 1

            while queue:        #사실상 bfs
                y, x = queue.popleft()
                for i in range(4):
                    next_x = x + move_x[i]
                    next_y = y + move_y[i]
                    if 0 <= next_x < m and 0 <= next_y < n:
                        if cabbage_patch[next_y][next_x] == 1:
                            cabbage_patch[next_y][next_x] = 2
                            queue.append([next_y, next_x])

for _ in range(input()):
    m, n, k = map(int,input().split())
    cabbage_patch = [[0]*m for _ in range(n)]
    cabbages = []
    for _ in range(k):
        x, y = map(int,input().split())
        cabbage_patch[y][x] = 1
        cabbages.append([y, x])