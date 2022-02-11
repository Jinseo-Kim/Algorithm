
max_size = int(input())
apple = list()
locate = list()

# 사과의 값을 받고 x축의 오름차순으로 아니라면 y축의 오름차순으로 정렬한다.
for _ in range(int(input())):
    apple.append(list(map(int,input().split())))

sorted(apple, key = lambda x : (x[0],x[1]))

# 위치의 값을 받고 각 방향 전환 시간과 rotate(오, 왼) 중 하나를 결정하도록 한다.
for _ in range(int(input())):
    locate.append(input().split())

while True:
    pass