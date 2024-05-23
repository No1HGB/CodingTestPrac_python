import sys

input = sys.stdin.readline

N, K = map(int, input().split())

grades = list(map(int, input().split()))

ranges = [list(map(int, input().split())) for _ in range(K)]

prefix = [0] * (N + 1)

for i in range(len(grades)):
    prefix[i + 1] = prefix[i] + grades[i]


for r in ranges:
    answer = (prefix[r[1]] - prefix[r[0] - 1]) / (r[1] - r[0] + 1)
    answer = round(answer, 2)
    formatted_answer = f"{answer:.2f}"
    print(formatted_answer)
