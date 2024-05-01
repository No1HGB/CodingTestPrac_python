import sys

input = sys.stdin.readline

N, H = map(int, input().split())

odd_hurdles = [0] * (H + 1)
even_hurdles = [0] * (H + 1)

for i in range(1, N + 1):
    h = int(input())
    if i % 2 == 1:
        # 끝점과 시작점
        odd_hurdles[H - h] += 1
        odd_hurdles[H] -= 1
    else:
        # 끝점과 시작점
        even_hurdles[-(H - h + 1)] += 1
        even_hurdles[-(H + 1)] -= 1

# 누적합계산
for i in range(1, H + 1):
    odd_hurdles[i] += odd_hurdles[i - 1]
    even_hurdles[-(i + 1)] += even_hurdles[-i]

# 배열 0 부분 삭제
odd_hurdles = odd_hurdles[:-1]
even_hurdles = even_hurdles[1:]

sum_hurdles = [a + b for a, b in zip(odd_hurdles, even_hurdles)]

min_hurdle = min(sum_hurdles)
min_count = sum_hurdles.count(min_hurdle)
print(f"{min_hurdle} {min_count}")
