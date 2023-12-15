"""
https://softeer.ai/practice/6277
[HSAT 2회 정기 코딩 인증평가 기출] 사물인식 최소 면적 산출 프로그램
"""

import sys


def solution():
    N, K = map(int, input().split())

    points = [[] for _ in range(K)]
    for _ in range(N):
        x, y, k = map(int, input().split())
        points[k - 1].append([y, x])
    # print(points)

    global answer
    answer = float("inf")

    def recur(ly, lx, ry, rx, num, current):
        global answer
        if num == K:
            answer = min(answer, current)
            return

        for y, x in points[num]:
            y1, x1, y2, x2 = ly, lx, ry, rx
            if y < ly:
                y1 = y
            elif y > ry:
                y2 = y
            if x < lx:
                x1 = x
            elif x > rx:
                x2 = x

            temp = abs(y2 - y1) * abs(x2 - x1)
            if temp < answer:
                recur(y1, x1, y2, x2, num + 1, temp)

    for y, x in points[0]:
        recur(y, x, y, x, 1, 0)
    return answer


if __name__ == "__main__":
    print(solution())
