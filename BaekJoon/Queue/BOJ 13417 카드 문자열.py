from collections import deque
import sys

for _ in range(int(input())):
    N = int(input())
    cards = deque(sys.stdin.readline().split())
    result = deque()

    for _ in range(N):
        card = cards[0]
        result.append(cards.popleft())
        if result[0] <= result[-1]:
            result.appendleft(card)
        else:
            result.append(card)

    print(''.join(result))