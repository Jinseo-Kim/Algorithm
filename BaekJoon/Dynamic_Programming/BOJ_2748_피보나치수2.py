# https://www.acmicpc.net/problem/2748
# 예제 입력 : 10
# 예제 출력 : 55

def fibonacci(n, dp_table):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp_table[n] != 0:
        return dp_table[n]

    dp_table[n] = fibonacci(n-1, dp_table) + fibonacci(n-2, dp_table)

    return dp_table[n]

dp_table = [0] * 91
dp_table[1] = 1
print(fibonacci(int(input()), dp_table))
