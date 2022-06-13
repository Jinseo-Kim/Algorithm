n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
result = 0

while k != 0:
    slice = coin.pop()

    if k // slice != 0:
        result += k // slice
    k = k % slice

print(result)
