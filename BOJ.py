# 50 | 30 24 5 28 45 | 98 52 60
# 5 28 24 45 30 | 60 52 98 | 50

# import sys
# sys.setrecursionlimit(10**6)

# def pre_order(tree):
#     # root = tree[0]

#     if len(tree) <= 1:
#         return tree[0]
    
#     for i in range(1,len(tree)):
#         if tree[0] < tree[i]:
#             return pre_order(tree[1:i]) + pre_order(tree[i:]) + tree[0]
    
#     return tree




# tree = [i for i in int(sys.stdin.readline())]
# pre_order(tree)


class stack:
    def __init__(self) -> None:
        self.stack = []
        self.cnt = 0
    def push(self, num):
        self.stack.append(num)
        self.cnt += 1
    

    def pop(self):
        if self.cnt == 0:
            print(-1)
        else:
            self.stack.pop()
            self.cnt -= 1

    def size(self):
        print(self.cnt)

    def top(self):
        if self.cnt == 0:
            print(-1)
        else:
            print(self.stack[-1])

    def empty(self):
        if self.cnt == 0:
            print(1)
        else:
            print(0)


st = stack()
for _ in range(int(input())):
    test_list = input().split()

    if test_list[0] == 'push':
        st.push(test_list[1])
        continue

    if test_list[0] == 'pop':
        pass
        continue

    if test_list[0] == 'size':
        pass
        continue
    
    if test_list[0] == 'top':
        pass
        continue

    if test_list[0] == 'empty':
        pass
        continue