# BOJ 2460 지능형 기차2

import sys

people = 0
max = 0

for _ in range(10):
    off_train, on_train = map(int,sys.stdin.readline().split())

    if max == 0:
        max += on_train
        people += on_train
    else:
        people += (on_train - off_train)

    if people > max:
        max = people
print(max)