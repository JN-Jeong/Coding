"""
https://softeer.ai/practice/6292
수퍼바이러스
"""

import sys


def solution():
    answer = 0
    k, p, n = map(int, input().split())

    def recur(p, n):
        if n == 1:
            return p
        elif n % 2 == 0:
            result = recur(p, n // 2)
            return (result * result) % 1000000007
        elif n % 2 == 1:
            result = recur(p, n // 2)
            return (result * result * p) % 1000000007

    answer = (k * recur(p, n * 10)) % 1000000007

    return answer


if __name__ == "__main__":
    print(solution())
