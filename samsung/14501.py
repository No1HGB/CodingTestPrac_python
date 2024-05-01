# 동적 프로그래밍(dynamic programming)

import sys

input = sys.stdin.readline


T = []
P = []
N = int(input())

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# mp[i]는 i일날 얻을 수 있는 최대 수익(기대 수익), 현재 0일.
mp = [0] * (N + 1)

# 역순으로 생각. 6일 최대 수익 = 당일(6일) + 7일 최대 수익 or 7일 최대 수익(당일 상담 불가)
for i in range(N, -1, -1):
    # 당일 상담 가능
    if T[i - 1] + i - 1 < N + 1:
        mp[i - 1] = max(P[i - 1] + mp[i - 1 + T[i - 1]], mp[i])
    # 당일 상담 불가능
    else:
        mp[i - 1] = mp[i]

print(mp[0])
