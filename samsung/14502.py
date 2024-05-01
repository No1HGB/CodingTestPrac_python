# BFS(너비 탐색 이론)

import sys
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline


def find_locs(lab: list, number: int, N: int, M: int) -> list:
    locs = []
    for y in range(N):
        for x in range(M):
            if lab[y][x] == number:
                locs.append([y, x])

    return locs


def spread_virus(lab, virus_locs, N, M):
    # 우,좌,상,하
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 바이러스 좌표 리스트를 슬라이싱해서 복사본 생성 후 큐에 저장(슬라이싱을 하는 경우 복사본 생성)
    queue = virus_locs[:]

    # 큐가 비어있을때까지 계속 반복
    while queue:
        # list.pop(index) => 리스트의 특정 인덱스의 원소를 삭제하고 반환.
        # 첫 번째 원소 y,x 할당
        y, x = queue.pop(0)
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            # 움직인 좌표가 0이상 최댓값 미만이고, 움직인 좌표의 값이 0이면,
            if 0 <= ny < N and 0 <= nx < M and lab[ny][nx] == 0:
                lab[ny][nx] = 2
                # 바이러스가 퍼질 수 있도록 큐에 좌표 추가.
                queue.append((ny, nx))
                # 이후 바이러스가 전부 퍼지고 pop으로 큐가 전부 비워질 때까지 반복.


def count_safe_zone(lab: list) -> int:
    return sum(row.count(0) for row in lab)


N, M = map(int, input().split())

lab_original = [list(map(int, input().split())) for _ in range(N)]

# 실험실 빈 방 좌표들
zero_locs = find_locs(lab_original, 0, N, M)

# 실험실 바이러스 좌표들
virus_locs = find_locs(lab_original, 2, N, M)

count_list = []

max_safe_area = 0
for walls in combinations(zero_locs, 3):
    # 깊은 복제(내부 구성까지 전부 복제)
    lab = deepcopy(lab_original)
    for y, x in walls:
        lab[y][x] = 1

    lab_virus = spread_virus(lab, virus_locs, N, M)
    max_safe_area = max(max_safe_area, count_safe_zone(lab))

print(max_safe_area)
