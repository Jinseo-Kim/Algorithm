def solution(prices):
    result = []

    for i in range(len(prices)-1):
        for j in range(1,len(prices)-i):
            if prices[i] > prices[i+j]:
                break

        result.append(j)

    result.append(0)
    return result

print(solution([1,2,3,2,3]))