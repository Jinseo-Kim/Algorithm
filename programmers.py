def solution(L, x):
    answer = []

    for i,j in enumerate(L):
        if L.count(x) == 0:
            answer.append(-1)
            break

        if j == x:
            answer.append(i)

    return answer

L = [64, 72, 83, 72, 54]
x = 49
print(solution(L,x))
