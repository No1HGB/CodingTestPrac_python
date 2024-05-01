# DFS
# 재귀 함수가 두 개 있는 경우 이진 트리 구조와 동일
import sys

input = sys.stdin.readline


def dfs(S: list, N: int, start: list, link: list, depth, start_visited: list):
    if depth == N:
        if len(start) == N // 2 and len(link) == N // 2:
            sum_start = sum(S[i][j] for i in start for j in start)
            sum_link = sum(S[i][j] for i in link for j in link)
            return abs(sum_start - sum_link)
        else:
            return float("inf")
    if len(start) > N or len(link) > N:
        return float("inf")

    # 스타트 팀
    start_visited[depth] = True
    start.append(depth)
    diff_1 = dfs(S, N, start, link, depth + 1, start_visited)
    start_visited[depth] = False  # 백트래킹
    start.pop()  # 백트래킹

    # 링크 팀
    link.append(depth)
    diff_2 = dfs(S, N, start, link, depth + 1, start_visited)
    link.pop()

    return min(diff_1, diff_2)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
min_cal = dfs(S, N, [], [], 0, [False] * N)
print(min_cal)
