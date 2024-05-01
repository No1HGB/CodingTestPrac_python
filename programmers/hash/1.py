# 내 풀이


def solution(nums):
    num_list = []
    for num in nums:
        if num in num_list:
            pass
        else:
            num_list.append(num)

    N = len(nums)
    answer = 0
    if len(num_list) < N / 2:
        answer = len(num_list)
    else:
        answer = N / 2
    return answer


# 최적 풀이
def solution(ls):
    return min(len(ls) / 2, len(set(ls)))
