"""
https://softeer.ai/practice/6270
GBC
"""

import sys


def solution():
    N, M = map(int, input().split())
    limits = [list(map(int, input().split())) for _ in range(N)]
    test_limits = [list(map(int, input().split())) for _ in range(M)]

    answer = 0
    for l, s in limits:
        for i in range(len(test_limits)):
            tl, ts = test_limits[i]
            if l > 0 and tl > 0:
                answer = max(answer, ts - s)
                l, tl = max(0, l - tl), max(0, tl - l)
                test_limits[i][0] = tl

    return answer


if __name__ == "__main__":
    print(solution())
