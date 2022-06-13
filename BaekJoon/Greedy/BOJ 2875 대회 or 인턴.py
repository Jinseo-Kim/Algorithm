n, m, k = map(int, input().split())
result = 0
max_team = n // 2

if max_team <= m:
    result += max_team
else:
    result += m

if m+n - (result * 3) >= k:
    print(result)
else:
    print(int(result - (k - (m+n - (result * 3))) / 3))
