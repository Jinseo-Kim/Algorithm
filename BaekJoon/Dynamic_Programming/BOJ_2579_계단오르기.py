# https://www.acmicpc.net/problem/2579
# 예제 입력
# 6
# 10
# 20
# 15
# 25
# 10
# 20
# 예제 출력
# 75

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.reverse()
dp_table = arr[0] + [0]*(n-1)

for order in range(1, n):
    if arr[order] == arr[order-1]:
        dp_table[order] += arr[order-1]
        continue
    
