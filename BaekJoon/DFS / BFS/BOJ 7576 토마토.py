from collections import deque
import sys

def bfs(tomato_box, ripe_tomato, m, n, dx, dy):
    queue = deque()


m, n = map(int, input().split())
tomato_box = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,1,-1]     #dx = direction_x, dy = direction_y
ripe_tomato = []
for y in range(n):
    for x in range(m):
        if tomato_box[y][x] == 1:
            ripe_tomato.append([y,x])

bfs(tomato_box, ripe_tomato, m, n, dx, dy)