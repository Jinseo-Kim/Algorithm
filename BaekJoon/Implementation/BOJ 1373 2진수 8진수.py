# BOJ 1373 2진수 8진수
# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

num = '0b'+input()
print(oct(int(num, 2))[2:])