# 리스트 슬라이싱을 기억하자
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        if j < len(array):
            arr = array[i - 1 : j]
        else:
            arr = array[i - 1 :]

        arr.sort()
        answer.append(arr[k - 1])

    return answer
