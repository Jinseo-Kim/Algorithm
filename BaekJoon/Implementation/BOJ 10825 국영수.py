# BOJ 10825 국영수

# 도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
# 1. 국어 점수가 감소하는 순서로
# 2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로(단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

import sys

do_class =[]
for _ in range(int(input())):
    result = [int(j) if i > 0 else j for i,j in enumerate(sys.stdin.readline().split())]
    do_class.append(result)

do_class.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in do_class:
    print(i[0])