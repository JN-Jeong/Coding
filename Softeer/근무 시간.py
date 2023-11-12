"""
https://softeer.ai/practice/6254
근무 시간
"""

import sys


def solution():
    def hour2minute(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    answer = 0
    for _ in range(5):
        start, end = input().split()
        answer += hour2minute(end) - hour2minute(start)

    return answer


if __name__ == "__main__":
    print(solution())
