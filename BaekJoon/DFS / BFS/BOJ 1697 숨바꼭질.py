N, K = map(int,input().split())

# 수빈이 = N
# 동생 = K

# 방법 1.
# N의 값을 -1 +1 2* 한다음 그 모든 값들을 리스트에 넣고 함수에 적용한다.
# 함수의 안에서 해당 값을 -1 +1 2*를 하고 해당 리스트의 [0] [-1] 사이에 target 값이 없다면 아무것도 리턴하지 않고
# 값이 있다면 계속해서 재귀 함수를 실행한다.

# result 리스트에 timer 값을 각각 하나씩 넣고 마지막 조건문에서 O(n) 반복으로 sort를 실행하고 가장 앞의 값을 반환한다.

def bfs(move_point, result, target, timer = 0):
    if timer != 0:
        if move_point[0] > target or target > move_point[-1]:
            return

    timer += 1
    
    for i in move_point:
        if i == target:
            result.append(timer)
            return result
        else:
            bfs([i-1, i+1, 2*i], result, target, timer)

    return result

if __name__ == '__main__':
    result = []
    print(bfs([N-1, N+1, 2*N], result, K))
    # sorted(bfs([N-1, N+1, 2*N], result, K))