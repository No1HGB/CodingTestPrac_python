def solution(numbers):
    numbers_str = list(map(str, numbers))

    # 자릿수 확장 비교를 위해 수를 여러번(여기선 3번) 반복. '3' => '333'/'30'=>'303030'
    numbers_str.sort(key=lambda x: x * 4, reverse=True)

    # 리스트 내 문자열 합치기
    answer = "".join(numbers_str)

    # 모든 숫자가 0인 경우, '000...' 대신 '0'을 리턴
    return answer if answer[0] != "0" else "0"
