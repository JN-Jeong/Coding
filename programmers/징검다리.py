"""
프로그래머스 : 징검다리
"""


def solution(distance, rocks, n):
    answer = 0
    rocks = sorted(rocks) + [distance]
    print("@", rocks)

    start = 0
    end = distance + 1

    while start <= end:
        mid = (start + end) // 2
        del_stone = 0  # 제거한 돌 개수
        pre_stone = 0  # 기준이 되는 돌 위치
        for rock in rocks:
            if rock - pre_stone < mid:  # 돌 사이의 거리가 가정한 값보다 작으면 제거
                del_stone += 1

            else:  # 그렇지 않으면 그 돌을 새로운 기준으로 설정
                pre_stone = rock

            if del_stone > n:
                break

        if del_stone > n:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer


if __name__ == "__main__":
    distance = [25, 4]
    rocks = [[2, 14, 11, 21, 17], [1, 2, 3]]
    n = [2, 2]
    results = [4, 2]

    for i, data in enumerate(zip(distance, rocks, n)):
        d, r, n = data
        print(f"#{i}", solution(d, r, n))
