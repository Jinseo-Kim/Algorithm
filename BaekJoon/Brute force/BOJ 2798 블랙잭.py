from itertools import combinations, permutations


n, m = map(int,input().split())
num_list = list(map(int,input().split()))
permu_list = [0 if sum(i) > m else sum(i) for i in list(permutations(num_list, 3))]
permu_list = set(permu_list)
result = 0
perfect_num = m

for num in permu_list:
    if num != 0 and m-num < perfect_num:
        result = num
        perfect_num = m-num

print(result)
        