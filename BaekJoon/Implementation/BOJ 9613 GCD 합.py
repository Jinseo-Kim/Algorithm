# BOJ 9613 GCD 합
# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다
# 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다.
from itertools import combinations
import sys


def gcd(ncm):
    while True:
        if ncm[1] > ncm[0]:
            ncm[0], ncm[1] = ncm[1], ncm[0]

        if ncm[0] % ncm[1] == 0:
            return ncm[1]

        ncm[0] = ncm[0] % ncm[1] 


for _ in range(int(input())):
    result = 0
    n, *nums = map(int,sys.stdin.readline().split())
    unpack_nums = list(map(list, combinations(nums,2)))

    for ncm in unpack_nums:
        result += gcd(ncm)
    print(result)