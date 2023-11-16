"""
https://softeer.ai/practice/6291
강의실 배정
"""

import sys


def solution():
    answer = 0
    N = int(input())
    lectures = [list(map(int, input().split())) for _ in range(N)]
    lectures = sorted(lectures, key=lambda x: x[1])
    # print(lectures)

    prev = 0
    for start, end in lectures:
        if prev <= start:
            prev = end
            answer += 1

    return answer


print(solution())
