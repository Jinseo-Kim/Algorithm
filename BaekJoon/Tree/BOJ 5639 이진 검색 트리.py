# 50 | 30 24 5 28 45 | 98 52 60
# 5 28 24 45 30 | 60 52 98 | 50

import sys
sys.setrecursionlimit(10**6)

def pre_order(tree):
    # root = tree[0]

    if len(tree) <= 1:
        return tree[0]

    for i in range(1,len(tree)):
        if tree[0] < tree[i]:
            return pre_order(tree[1:i]) + pre_order(tree[i:]) + tree[0]

    return tree
