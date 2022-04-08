N = int(input())
result = 0

while True:
    if N % 5 == 0:
        result += (N // 5)
        break
    if N % 3 == 0:
        result += (N // 3)
        break

    if N > 3:
        if N // 5 != 0:
            N -= 5
            result += 1
    else:
        result = -1
        break

print(result)
    
# 조건을 생각해보자
# 1. N이 주어진다
# 2. N을 주어진 5와 3으로 나눈다
# 2-1. 가장 큰 수로 먼저 나누기를 시도한다.
# 2-2. 이후 나머지를 3으로 나눈다.
# 돌지 못하는 조건 = 5로 나눈 나머지가 3보다 작거나 3으로 나눈 나머지가 3보다 작다면 돌지 못한다.
# 3. 최적의 개수를 구한다.

