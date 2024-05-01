# 파이썬 순열
from itertools import permutations

lst = [1, 2, 3, 4, 5, 6]

perm_lst = list(permutations(lst))

for perm in perm_lst:
    print(list(perm))


# 순열 직접 구현
def permute(lst):
    # 결과를 담을 리스트
    result = []

    # 종료 조건: 리스트의 길이가 1 이하일 때
    if len(lst) <= 1:
        return [lst]

    # 리스트의 각 원소에 대해
    for i in range(len(lst)):
        # 현재 원소를 제외한 나머지 리스트
        n = lst[:i] + lst[i + 1 :]
        # 나머지 리스트에 대한 순열
        for p in permute(n):
            result.append([lst[i]] + p)

    return result


lst = [1, 2, 3, 4, 5, 6]

perm_lst = permute(lst)

for perm in perm_lst:
    print(perm)
