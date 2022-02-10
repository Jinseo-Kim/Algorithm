from collections import deque
import sys

for _ in range(int(input())):
    N = int(input())
    cards = deque(sys.stdin.readline().split())
    result = deque()

    for _ in range(N):
        card = cards.popleft()
        
        if result:
            if result[0] >= card:
                result.appendleft(card)
            else:
                result.append(card)
        else:
            result.append(card)

    print(''.join(result))