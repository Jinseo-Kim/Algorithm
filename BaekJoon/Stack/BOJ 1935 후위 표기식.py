# BOJ 1935 후위 표기식
# 1. postfix의 횟수만큼 순회
# 2. 각 숫자를 입력받고 영어대문자가 나올 때마다 입력.

import sys

N = int(input())
postfix = list(input())
stack = []
cnt = 0

for i in postfix:
    if i == '+':
        stack.append(stack.pop()+stack.pop())
    elif i == '-':
        last = stack.pop()
        stack.append(stack.pop()-last)
    elif i == '*':
        stack.append(stack.pop()*stack.pop())
    elif i == '/':
        last = stack.pop()
        stack.append(stack.pop()/last)
    else:
        if cnt == N:
            stack.append(solo)
        if cnt != N:
            stack.append(int(sys.stdin.readline()))
            solo = stack[0]
            cnt += 1
print(format(*stack,".2f"))