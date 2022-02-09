# BOJ 9012 괄호
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.


# 1. T번 반복하며 입력받기
# 2. 각 횟수당 YES, NO 형태로 출력하기
# - 조건 : 시작하는 문자열이 )이면 안되며, 끝나는 문자열이 (이면 안된다.
#         괄호의 개수는 짝수여야한다.
#         스택을 통해 구현하며 ( 괄호를 더하고 )을 만나면 하나씩 pop한다. 이후 마지막까지 돌았으나 잔여 스택의 개수가 0이면 YES

import sys

for _ in range(int(input())):
    stack = []
    vps = sys.stdin.readline().strip()

    if len(vps) % 2 == 1:
        print('NO')

    elif vps[0] == ')' or vps[-1] == '(':
        print('NO')

    else:
        for i in vps:
            if i == '(':
                stack.append('(')
            if i == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    stack.append('underflow')
                    break

        if len(stack) > 0:
            print('NO')
        else:
            print('YES')