"""
프로그래머스 : 두 원 사이의 정수 쌍
"""
import math


def solution(r1, r2):
    answer = 0
    for y in range(1, r2 + 1):
        if (r1 * r1 - y * y) > 0:
            min_x = math.ceil((r1 * r1 - y * y) ** 0.5)
        else:
            min_x = 0
        max_x = math.floor((r2 * r2 - y * y) ** 0.5)
        print("@", max_x, min_x)
        answer += max_x - min_x + 1
        print("@@", answer)

    return answer * 4


if __name__ == "__main__":
    r1s = [2, 2]
    r2s = [3, 5]
    results = [20]

    for i, data in enumerate(zip(r1s, r2s)):
        r1, r2 = data
        print(f"#{i}", solution(r1, r2))
