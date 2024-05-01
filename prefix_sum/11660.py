import sys

input = sys.stdin.readline


def calculate_prefix_sum(N, matrix):
    prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix_sum[i][j] = (
                matrix[i - 1][j - 1]
                + prefix_sum[i][j - 1]
                + prefix_sum[i - 1][j]
                - prefix_sum[i - 1][j - 1]
            )

    return prefix_sum


def calculate_result(M, points, prefix_sum):
    for i in range(M):
        x1 = points[i][0]
        y1 = points[i][1]
        x2 = points[i][2]
        y2 = points[i][3]

        result = (
            prefix_sum[x2][y2]
            - prefix_sum[x1 - 1][y2]
            - prefix_sum[x2][y1 - 1]
            + prefix_sum[x1 - 1][y1 - 1]
        )
        print(result)
    return


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
points = [list(map(int, input().split())) for _ in range(M)]

prefix_sum = calculate_prefix_sum(N, matrix)
calculate_result(M, points, prefix_sum)
