# BOJ 2588 곱셈
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

first_num = int(input())
second_num = int(input())
arr_sec = [int(i) for i in str(second_num)]
arr_sec.reverse()

for i in arr_sec:
    print(first_num * i)

print(first_num * second_num)
