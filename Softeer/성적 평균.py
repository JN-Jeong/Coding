"""
https://softeer.ai/practice/6294
성적 평균
"""

import sys


def solution():
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    sum_scores = [0]
    for i in range(len(scores)):
        sum_scores.append(sum_scores[-1] + scores[i])

    for _ in range(k):
        a, b = map(int, input().split())
        print(round(((sum_scores[b] - sum_scores[a - 1]) / (b - a + 1)), 2))


if __name__ == "__main__":
    solution()
