"""
https://softeer.ai/practice/6253
주행거리 비교하기
"""

import sys


def solution():
    a, b = map(int, input().split())
    if a > b:
        return "A"
    elif a < b:
        return "B"
    else:
        return "same"


if __name__ == "__main__":
    print(solution())
