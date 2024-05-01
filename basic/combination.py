# 파이썬 조합
from itertools import combinations

lst = [1, 2, 3, 4, 5, 6]

comb_lst = list(combinations(lst, 3))

for comb in comb_lst:
    print(comb)


# 조합 직접 구현
def combine(lst, n):
    # 조합 결과를 저장할 리스트
    result = []

    # 실제 조합을 구하는 재귀 함수
    def dfs(elements, start, k):
        # 하나의 조합이 완성될 때 결과에 추가
        if k == 0:
            result.append(elements[:])
            return

        # 주어진 리스트를 순회하면서 조합 생성
        for i in range(start, len(lst)):
            elements.append(lst[i])
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 0, n)
    return result


lst = [1, 2, 3, 4, 5, 6]

comb_lst = combine(lst, 3)

for comb in comb_lst:
    print(comb)
