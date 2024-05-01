# 큐
# 구현 시 순서와 단계적 절차를 중요하게 생각할 것.

N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수
apples = {tuple(map(int, input().split())) for _ in range(K)}  # 사과의 위치
L = int(input())  # 방향 변환 횟수
directions = [input().split() for _ in range(L)]  # 방향 변환 정보

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, C):
    if C == "L":
        direction = (direction - 1) % 4
    else:  # 'D'의 경우
        direction = (direction + 1) % 4
    return direction


# 시뮬레이션 시작
time = 0
x, y = 1, 1
snake = [(x, y)]  # 뱀이 차지하고 있는 위치들
direction = 0  # 초기 방향: 동쪽(index, 동,남,서,북:0,1,2,3)

for t, C in directions:
    t = int(t)
    while time < t:
        time += 1
        nx, ny = x + dx[direction], y + dy[direction]

        # 벽이나 자기자신의 몸과 부딪힌 경우
        if nx < 1 or nx > N or ny < 1 or ny > N or (nx, ny) in snake:
            print(time)
            exit(0)

        # 사과가 있는 경우
        if (nx, ny) in apples:
            apples.remove((nx, ny))
        else:  # 사과가 없는 경우
            snake.pop(0)

        snake.append((nx, ny))
        x, y = nx, ny

    direction = turn(direction, C)

# 방향 전환 후의 마지막 이동(마지막 이동은 위 while 문에서 구현되지 않았기 때문)
while True:
    time += 1
    nx, ny = x + dx[direction], y + dy[direction]
    if nx < 1 or nx > N or ny < 1 or ny > N or (nx, ny) in snake:
        print(time)
        break
    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        snake.pop(0)
    snake.append((nx, ny))
    x, y = nx, ny
