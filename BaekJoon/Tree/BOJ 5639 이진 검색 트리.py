# 50 | 30 24 5 28 45 | 98 52 60
# 5 28 24 45 30 | 60 52 98 | 50

import sys
sys.setrecursionlimit(10**6)


def post_order(tree):
    if len(tree) <= 1:
        return tree

    for i in range(1, len(tree)):
        if tree[0] < tree[i]:
            return post_order(tree[1:i]) + post_order(tree[i:]) + [tree[0]]

    return post_order(tree[1:]) + [tree[0]]


tree = []
while True:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break

nums = post_order(tree)
for i in nums:
    print(i)