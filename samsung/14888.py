# DFS(깊이 탐색 이론) : 트리 구조임. 각 재귀 함수 내 for 문이 각각 실행되는 구조
# for문이 종료되면 백트래킹으로 트리 위로 올라갈 수 있게 함

import sys

input = sys.stdin.readline


def calculate(current_value: int, next_value: int, cal):
    if cal == "+":
        result = current_value + next_value
    elif cal == "-":
        result = current_value - next_value
    elif cal == "*":
        result = current_value * next_value
    elif cal == "/":
        if current_value < 0:
            result = -((-current_value) // next_value)
        else:
            result = current_value // next_value

    return result


def dfs(nums: list, cals_count: list, index, current_value):
    if index == len(nums):
        global max_value, min_value
        max_value = max(max_value, current_value)
        min_value = min(min_value, current_value)
        return

    for i, cal in enumerate(cals_count):
        if cal > 0:
            cals_count[i] -= 1
            next_value = calculate(current_value, nums[index], "+-*/"[i])
            dfs(nums, cals_count, index + 1, next_value)
            # 백트래킹
            cals_count[i] += 1


N = int(input())
nums = list(map(int, input().split()))
cals_count = list(map(int, input().split()))
max_value, min_value = -float("inf"), float("inf")
dfs(nums, cals_count, 1, nums[0])
print(max_value)
print(min_value)
