"""
https://softeer.ai/practice/6293
징검다리
"""

import sys


def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    if N == 1:
        return 1

    rocks = [1] * len(arr)

    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                rocks[i] = max(rocks[i], rocks[j] + 1)
                answer = max(answer, rocks[i])
        print("@", rocks)

    return answer


if __name__ == "__main__":
    print(solution())
