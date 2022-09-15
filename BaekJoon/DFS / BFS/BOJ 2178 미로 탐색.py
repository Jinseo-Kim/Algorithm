from collections import deque

def bfs(n, m, maze, count = 0):
    queue = deque([[1,1]])
    maze[1][1] = '2'
    move_y, move_x = [-1,1,0,0], [0,0,-1,1]
    while queue:
        count += 1
        for _ in range(len(queue)):
            coordinate = queue.popleft()
            if coordinate[0] == n and coordinate[1] == m:
                return count

            for direction in range(4):
                next_y = coordinate[0] + move_y[direction]
                next_x = coordinate[1] + move_x[direction]
                if 0 < next_x <= m and 0 < next_y <= n:
                    if maze[next_y][next_x] == '1':
                        queue.append([next_y, next_x])
                        maze[next_y][next_x] = '2'



n, m = map(int,input().split())
maze = [[False]*m] + [[False] + list(input()) for _ in range(n)]
print(bfs(n, m, maze))