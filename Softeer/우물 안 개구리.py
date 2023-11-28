"""
https://softeer.ai/practice/6289
우물 안 개구리
"""

import sys


def solution():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    members = [1] * N

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1

        if W[a] <= W[b]:
            members[a] = 0
        if W[a] >= W[b]:
            members[b] = 0

    # print("@", members)
    answer = 0
    for i in range(N):
        answer += members[i]

    return answer


if __name__ == "__main__":
    print(solution())
