# https://www.acmicpc.net/problem/9095
# 예제 입력
# 3
# 4
# 7
# 10
# 예제 출력
# 7
# 44
# 274

def add_num(n, current, cnt):
    for loop_value in [1, 2, 3]:
        add_value = current + loop_value

        if add_value >= n:
            if add_value == n:
                cnt[0] += 1
            return cnt
        
        add_num(n, add_value, cnt)
    
    return cnt

for _ in range(int(input())):
    print(*add_num(int(input()), current = 0, cnt = [0]))