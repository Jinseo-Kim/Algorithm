# BOJ 1874 스택 수열
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
# 첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

# 문제 초기 생각
# main() - while문 구성
# 수를 하나씩 넣어가며 스택 top에 있는 수와 동일한 지 비교.
# 동일하다면 - 출력 ㅇㅇ
# 동일하지 않다면 + 출력 ㅇㅇ

# 기본 변수
# 함수 밖 input() 초기 변수를 주고 pop의 순간에 input()을 다시 새로 받아 해당 변수의 값을 초기화.
# 값을 증감해가며 스택에 저장해 줄 변수 cnt 필요. cnt = 1  / cnt += 1

# 불가능(NO)의 경우를 출력하기 위한 if조건문 구성
# top에 있는 값보다 작을 경우.
import sys

n = int(input())
push_num = int(input())
cnt = 0
stack = []
result = []

while True:
    if len(stack) > 0 and (push_num == stack[-1]):
        stack.pop()
        result.append('-')
        if cnt == n and len(stack) == 0:
            break
        push_num = int(sys.stdin.readline())
    else:
        cnt += 1
        stack.append(cnt)
        result.append('+')

    if len(stack) > 0 and (stack[-1] > push_num):
        result.append('NO')
        print('NO')
        break

if result[-1] != 'NO':
    for i in result:
        print(i)