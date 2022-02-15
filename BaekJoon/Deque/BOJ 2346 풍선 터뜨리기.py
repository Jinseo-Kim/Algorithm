from collections import deque

N = int(input())
baln = deque(list(map(int,input().split())))
arr = deque(range(1,N+1))
result = []

result.append(arr.popleft())
move = baln.popleft()

for _ in range(N):
    if not baln:
        print(*result)
        break

    if move > 0:
        arr.rotate(-move+1)
        baln.rotate(-move+1)
        result.append(arr.popleft())
        move = baln.popleft()
    else:
        arr.rotate(abs(move)-1)
        baln.rotate(abs(move)-1)
        result.append(arr.pop())
        move = baln.pop()

# while True:
#     if not baln:
#         print(*result)
#         break
    
#     if move > 0:
#         for i in range(move-1):
#             baln.append(baln.popleft())
#             arr.append(arr.popleft())

#         result.append(arr.popleft())
#         move = baln.popleft()

#     if move < 0:
#         for i in range(move,-1):
#             baln.appendleft(baln.pop())
#             arr.appendleft(arr.pop())

#         result.append(arr.pop())
#         move = baln.pop()

