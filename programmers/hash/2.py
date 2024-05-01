def solution(participant, completion):
    # 두 목록을 알파벳 순으로 정렬합니다.
    participant.sort()
    completion.sort()

    # 참가자 목록과 완주자 목록을 비교합니다.
    for i in range(len(completion)):
        # 완주하지 못한 선수를 찾으면 반환합니다.
        if participant[i] != completion[i]:
            return participant[i]

    # 모든 완주자를 비교한 후, 남은 마지막 참가자가 완주하지 못한 선수입니다.
    return participant[-1]
