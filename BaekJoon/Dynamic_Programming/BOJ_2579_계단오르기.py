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
dp_table = [1] * n

for order in range(n):
    if order >= n-1:
        if dp_table[order] != 2:
            arr[-1] += arr[order]
        break

    if dp_table[order] == 1:
        if arr[order] + arr[order+1] >= arr[order] + arr[order+2]:
            arr[order+1] += arr[order]
            dp_table[order+1] = 2
            dp_table[order+2] = 0
        else:
            arr[order+2] += arr[order]
            dp_table[order+1] = 0
    
    if dp_table[order] == 2:
        arr[order+2] += arr[order]
        dp_table[order+2] = 1

print(arr)