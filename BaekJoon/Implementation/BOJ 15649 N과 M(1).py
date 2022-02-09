# BOJ 15649 N과 M (1)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

from itertools import permutations

N, M = map(int,input().split())
N = list(range(1,N+1))

for i in permutations(N, M):
    print(*i)
