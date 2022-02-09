# BOJ 15828 Router

import sys

N = int(input())
queue = []
max_size = 0

while True:
    num = int(sys.stdin.readline())
    if num == -1:
        break
    if N > max_size and num != 0:
        queue.append(num)
        max_size += 1
    if num == 0:
        queue.pop(0)
        max_size -= 1

if not queue:
    print('empty')
else:
    print(*queue)
