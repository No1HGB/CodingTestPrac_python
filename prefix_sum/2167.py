import sys

input = sys.stdin.readline


def compute_prefix_sum(N, M, matrix):
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix_sum[i][j] = (
                matrix[i - 1][j - 1]
                + prefix_sum[i - 1][j]
                + prefix_sum[i][j - 1]
                - prefix_sum[i - 1][j - 1]
            )

    return prefix_sum


def compute_result(i, j, x, y, prefix_sum):
    result = (
        prefix_sum[x][y]
        - prefix_sum[x][j - 1]
        - prefix_sum[i - 1][y]
        + prefix_sum[i - 1][j - 1]
    )
    return result


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = compute_prefix_sum(N, M, matrix)

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = compute_result(i, j, x, y, prefix_sum)
    print(result)
