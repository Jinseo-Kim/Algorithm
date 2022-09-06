from collections import deque
import sys

def bfs(tomato_box, ripe_tomato, m, n, dx, dy, result = -1):
    while ripe_tomato:
        for _ in range(len(ripe_tomato)):
            y, x = ripe_tomato.popleft()

            for i in range(4):
                width = x + dx[i]
                height = y + dy[i]
                if 0 <= height < n and 0 <= width < m:
                    if tomato_box[height][width] == 0:
                        tomato_box[height][width] = 1
                        ripe_tomato.append([height,width])

        result += 1
    
    return result

m, n = map(int, input().split())
tomato_box = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,1,-1]     #dx = direction_x, dy = direction_y
ripe_tomato = deque()
for y in range(n):
    for x in range(m):
        if tomato_box[y][x] == 1:
            ripe_tomato.append([y,x])

result = (bfs(tomato_box, ripe_tomato, m, n, dx, dy))

for tomatoes in tomato_box:
    for tomato in tomatoes:
        if tomato == 0:
            result = -1

print(result)
