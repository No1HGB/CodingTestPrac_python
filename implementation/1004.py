import sys
import math

input = sys.stdin.readline


def distance(x, y, cx, cy):
    return math.sqrt((x - cx) ** 2 + (y - cy) ** 2)


def test_case():
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = distance(x1, y1, cx, cy)
        d2 = distance(x2, y2, cx, cy)
        if d1 < r and d2 > r:
            count += 1
        if d2 < r and d1 > r:
            count += 1

    print(count)
    return


T = int(input())

for _ in range(T):
    test_case()
