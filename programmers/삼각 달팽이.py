"""
월간 코드 챌린지 시즌1
삼각 달팽이
"""


def solution(n):
    answer = [[0 for j in range(1, i + 1)] for i in range(1, n + 1)]
    # print("@", answer)

    y, x = -1, 0
    num = 1

    for i in range(n):  # 방향
        for j in range(i, n):  # 좌표
            if i % 3 == 0:  # 하
                y += 1
            elif i % 3 == 1:  # 우
                x += 1
            else:  # 상
                y -= 1
                x -= 1
            answer[y][x] = num
            num += 1

    return sum(answer, [])


if __name__ == "__main__":
    ns = [4, 5, 6]
    answer = [
        [1, 2, 9, 3, 10, 8, 4, 5, 6, 7],
        [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9],
        [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11],
    ]

    for i, data in enumerate(ns):
        n = data
        print(f"#{i}", solution(n))
