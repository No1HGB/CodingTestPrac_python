def solution(clothes):
    kinds = []
    for cloth in clothes:
        kinds.append(cloth[1])
    # set/중복제거: O(n),순서보장x,집합자료형
    kinds = list(set(kinds))
    nums = [0] * len(kinds)
    for cloth in clothes:
        for i, kind in enumerate(kinds):
            if cloth[1] == kind:
                nums[i] += 1

    answer = 1
    for num in nums:
        answer *= num + 1

    return answer - 1
