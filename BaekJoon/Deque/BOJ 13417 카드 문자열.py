from collections import deque
import sys

for _ in range(int(input())):
    N = int(input())
    cards = sys.stdin.readline().split()
    result = deque()
    
    result.append(cards.pop(0))

    for i in cards:
        if result[0] >= i:
            result.appendleft(i)
        else:
            result.append(i)

    print(''.join(result))