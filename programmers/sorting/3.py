def solution(citations):
    citations.sort(reverse=True)  # 내림차순으로 정렬
    for i, citation in enumerate(citations):
        if citation >= i + 1:  # `i + 1`은 1부터 시작하는 논문의 수
            continue
        else:
            return i  # `i`는 현재 논문 수에서의 최대 H-Index
    return len(citations)  # 모든 인용 횟수가 논문 수보다 크거나 같은 경우
