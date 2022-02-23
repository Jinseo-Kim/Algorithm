A, B = map(int,input().split())
comp = 0
cnt = 0
result = []
while True:
    comp += cnt
    if B < comp:
        print(sum(result[A-1:B]))
        break
    cnt += 1
    for _ in range(cnt):
        result.append(cnt)