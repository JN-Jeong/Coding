"""
https://softeer.ai/practice/6290
징검다리2
"""

import bisect
import sys


def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    if N == 1:
        return 1

    dp_front = [arr[0]]
    dp_back = [arr[-1]]
    fronts = [1] * N
    backs = [1] * N

    # front
    for i in range(N):
        if arr[i] > dp_front[-1]:
            dp_front.append(arr[i])

        else:
            idx = bisect.bisect_left(dp_front, arr[i])
            print("#", idx, dp_front, arr[i])
            dp_front[idx] = arr[i]

        fronts[i] = len(dp_front)
        print("@", dp_front)

    # back
    for i in range(N - 1, -1, -1):
        if arr[i] > dp_back[-1]:
            dp_back.append(arr[i])
        else:
            idx = bisect.bisect_left(dp_back, arr[i])
            dp_back[idx] = arr[i]

        backs[i] = len(dp_back)
        print("@@", dp_back)

    for i in range(N):
        answer = max(answer, fronts[i] + backs[i])

    return answer - 1


if __name__ == "__main__":
    print(solution())
