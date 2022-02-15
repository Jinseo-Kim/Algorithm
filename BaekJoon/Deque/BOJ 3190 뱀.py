from collections import deque

max_size = int(input())
apple = deque()
locate = deque()
time = 0

# 사과의 값을 받고 x축의 오름차순으로 아니라면 y축의 오름차순으로 정렬한다.
for _ in range(int(input())):
    x, y = map(int,input().split())
    apple.append(x)
    apple.append(y)
    apple.append(x*y)

sorted(apple, key = lambda x : (x[0],x[1]))

# 위치의 값을 받고 각 방향 전환 시간과 rotate(오, 왼) 중 하나를 결정하도록 한다.
for _ in range(int(input())):
    locate.append(input().split())

# 뱀의 머리와 꼬리 (x,y) 좌표 값을 배열로 지정
snake_head = [1,1]
snake_tail = [1,1]
degree = 0
# 각도가 변할 때 snake_tail & snake_head의 x y 축 좌표가 달라진다. 이를 변수 2개를 만들 것인가 or 다른 해결책을 찾을 것인가...
# 하나의 리스트로 한다면?
# 0과 1을 기점으로 하나의 변수를 바꿔가며 값을 변화시키면 된다.

# 하지만 이에 대한 문제점은 무엇이 있을까?
# 위치 변수에 대한 것은 degree로 대체?? 0(x+1) 90(y+1) 180(x-1) 270(y-1)에 대한 값에 따라 처리 cell변수가 x,y 값을 정해준다면
# 사과의 경우 0번째 인덱스가 같으면 1번째 인덱스와 같은지 비교. 같다면 head만 증가시키고 tail은 그대로 둔다. 이후 다시 시작
crdnt = 0
while True:
    time +=1
    # x나 y에 + 해주는 진영
    if degree <= 90:
        if snake_head[crdnt]+1 == snake_tail[crdnt]:
            print(time)
            break
        for i in range(len(apple)):
            if apple[i][-1] > snake_head[0] * snake_head[1]:
                break
            if apple[i][-1] == snake_head[0] * snake_head[1]:
                if (snake_head[0] == apple[i][0]) and (snake_head[1] == apple[i][1]):
                    snake_head[crdnt] -= 1
                    for _ in range(i):
                        apple.append(apple.popleft())
                    apple.popleft()
                    
        snake_head[crdnt] += 1
        snake_tail[crdnt] += 1
    
    # x나 y에 - 해주는 진영
    if degree > 90:
        if snake_head[crdnt]-1 == snake_tail[crdnt]:
            print(time)
            break
        for i in range(len(apple)):
            if apple[i][-1] > snake_head[0] * snake_head[1]:
                break
            if apple[i][-1] == snake_head[0] * snake_head[1]:
                if (snake_head[0] == apple[i][0]) and (snake_head[1] == apple[i][1]):
                    snake_head[crdnt] -= 1
                    for _ in range(i):
                        apple.append(apple.popleft())
                    apple.popleft()
    
        snake_head[crdnt] -= 1
        snake_tail[crdnt] -= 1