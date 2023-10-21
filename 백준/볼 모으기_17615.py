"""
17615. 볼 모으기
"""


def solution():
    n = int(input())
    balls = input()

    answer = float("inf")
    # 오른쪽에 빨간색 모으기
    right_red = balls.rstrip("R")
    answer = min(answer, right_red.count("R"))

    # 오른쪽에 파란색 모으기
    right_blue = balls.rstrip("B")
    answer = min(answer, right_blue.count("B"))

    # 왼쪽 빨간색 모으기
    left_red = balls.lstrip("R")
    answer = min(answer, left_red.count("R"))

    # 왼쪽 파란색 모으기
    left_blue = balls.lstrip("B")
    answer = min(answer, left_blue.count("B"))

    print(answer)
    return


if __name__ == "__main__":
    solution()
