def solution(genres, plays):
    genres_plays_dict = {}  # 장르: 총 재생횟수
    genres_song_dict = {}  # 장르: [(재생횟수1, 고유번호1),(재생횟수2, 고유번호2)...]

    # 딕셔너리 데이터 구성
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genres_plays_dict:
            genres_plays_dict[genre] = 0
            genres_song_dict[genre] = []
        genres_plays_dict[genre] += play
        genres_song_dict[genre].append((play, i))

    # (재생횟수,고유번호) 리스트를 재생횟수 기준 내림차순, 재생횟수가 같은 경우 고유번호 오름차순
    # dict.keys(), dict.values() => list
    # sort()와 sorted() 차이
    for song in genres_song_dict.values():
        song.sort(key=lambda x: (-x[0], x[1]))

    # 총 재생횟수 내림차순에 따라 장르 정렬
    sorted_genres = sorted(
        genres_plays_dict.keys(), key=lambda x: genres_plays_dict[x], reverse=True
    )

    # 재생횟수가 많은 장르 순서대로 2개의 고유번호
    answer = []
    for genre in sorted_genres:
        count = len(genres_song_dict[genre])
        if count < 2:
            answer.append(genres_song_dict[genre][0][1])
        else:
            answer.append(genres_song_dict[genre][0][1])
            answer.append(genres_song_dict[genre][1][1])

    return answer
