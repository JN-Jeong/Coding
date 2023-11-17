"""
https://softeer.ai/practice/6284
바이러스
"""

import sys


def solution():
    answer = 0
    k, p, n = map(int, input().split())

    for _ in range(n):
        k = k * p
        k = k % 1000000007

    answer = k % 1000000007
    return answer


print(solution())
