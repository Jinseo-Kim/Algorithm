# https://www.acmicpc.net/problem/1463
# 예제 입력
# 2
# 10
# 예제 출력
# 1
# 3

n = int(input())
dp_table = [0, 0, 1, 1] # 0~3의 수를 1로 만들기까지 필요한 최소 연산 횟수

for i in range(4, n+1):
    dp_table.append(dp_table[i-1]+1)

    if dp_table[i] % 3 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i//3]+1)
    
    if dp_table[i] % 2 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i//2]+1)

print(dp_table)
