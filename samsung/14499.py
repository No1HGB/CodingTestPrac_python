# 주사위 자리 변경
def move(direction, dice_seat: list):
    seat = dice_seat[:]
    # 동
    if direction == 1:
        dice_seat[1] = seat[4]
        dice_seat[2] = seat[2]
        dice_seat[3] = seat[1]
        dice_seat[4] = seat[6]
        dice_seat[5] = seat[5]
        dice_seat[6] = seat[3]
    # 서
    elif direction == 2:
        dice_seat[1] = seat[3]
        dice_seat[2] = seat[2]
        dice_seat[3] = seat[6]
        dice_seat[4] = seat[1]
        dice_seat[5] = seat[5]
        dice_seat[6] = seat[4]
    # 북
    elif direction == 3:
        dice_seat[1] = seat[5]
        dice_seat[2] = seat[1]
        dice_seat[3] = seat[3]
        dice_seat[4] = seat[4]
        dice_seat[5] = seat[6]
        dice_seat[6] = seat[2]
    # 남
    elif direction == 4:
        dice_seat[1] = seat[2]
        dice_seat[2] = seat[6]
        dice_seat[3] = seat[3]
        dice_seat[4] = seat[4]
        dice_seat[5] = seat[1]
        dice_seat[6] = seat[5]

    return dice_seat


N, M, x, y, K = map(int, input().split())
dice_map = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위에 적혀 있는 숫자(주사위 1-6 자리는 인덱스 1-6으로 고정)
dice = [0] * 7
# 인덱스 1: 윗면, 인덱스 6: 아랫면
dice_seat = [i for i in range(7)]

for direction in commands:
    if direction == 1:
        dx, dy = 0, 1
    elif direction == 2:
        dx, dy = 0, -1
    elif direction == 3:
        dx, dy = -1, 0
    elif direction == 4:
        dx, dy = 1, 0

    if x + dx < 0 or x + dx > N - 1 or y + dy < 0 or y + dy > M - 1:
        pass
    else:
        x = x + dx
        y = y + dy
        dice_seat = move(direction, dice_seat)
        up = dice_seat[1]
        down = dice_seat[6]
        if dice_map[x][y] == 0:
            dice_map[x][y] = dice[down]
        else:
            dice[down] = dice_map[x][y]
            dice_map[x][y] = 0
        print(dice[up])
