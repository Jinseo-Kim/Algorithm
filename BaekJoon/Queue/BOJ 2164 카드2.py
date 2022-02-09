# BOJ 2164 카드2

from collections import deque

N = int(input())
deq = deque(range(1, N+1))

while True:
    if len(deq) == 1:
        print(deq[0])
        break
    deq.popleft()
    deq.append(deq.popleft())
