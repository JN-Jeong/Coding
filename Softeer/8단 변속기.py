"""
https://softeer.ai/practice/6283
8단 변속기
"""

import sys


def solution():
    arr = list(map(int, input().split()))

    if arr[0] > arr[1] and arr[0] - arr[1] == 1:  # descending
        flag = 0
    elif arr[0] < arr[1] and arr[1] - arr[0] == 1:  # ascending
        flag = 1

    for i in range(1, len(arr)):
        if abs(arr[i - 1] - arr[i]) != 1:
            return "mixed"

        elif arr[i - 1] > arr[i] and flag == 1:  # descending check
            return "mixed"

        elif arr[i - 1] < arr[i] and flag == 0:  # ascending check
            return "mixed"

    if flag == 0:
        return "descending"
    if flag == 1:
        return "ascending"


print(solution())
