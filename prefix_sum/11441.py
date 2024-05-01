import sys

input = sys.stdin.readline


N = int(input())
A_N = list(map(int, input().split()))
M = int(input())


def prefix_sum(A_N: list) -> list:
    for i in range(1, N):
        A_N[i] += A_N[i - 1]
    return A_N


S_N = prefix_sum(A_N)

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        result = S_N[j - 1]
    else:
        result = S_N[j - 1] - S_N[i - 2]
    print(result)
