# 누적 합 대신 two point 전략 사용
N, M = map(int, input().split())
A = list(map(int, input().split()))

interval_sum = 0  # 부분수열의 합
end = 0  # 부분수열의 끝점
count = 0  # 경우의 수

for start in range(N):
    # 부분수열의 합이 M이 될 때까지, 끝점이 N이 될 때까지 부분수열의 끝점을 더해준다.
    while interval_sum < M and end < N:
        interval_sum += A[end]
        end += 1

    # 부분수열의 합이 M이 되는 순간 경우의 수 +1
    if interval_sum == M:
        count += 1

    # 수열합의 시작점을 제거해준다.
    # 첫 번째를 제거하면 다시 while문이 작동하게 됨.
    # 즉, 어차피 이미 더해놨으니 첫 번째 수열만 제거하면 끝점을 뒤로 이동시키면서 수열합을 구할 수 있음.
    interval_sum -= A[start]

print(count)
