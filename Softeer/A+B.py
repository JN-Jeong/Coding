"""
https://softeer.ai/practice/6295
A+B
"""

import sys


def solution():
    answer = 0
    a, b = map(int, input().split())
    answer = a + b
    return answer


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        print(f"Case #{i+1}: {solution()}")
