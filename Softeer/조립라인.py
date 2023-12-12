"""
https://softeer.ai/practice/6287
조립라인
"""

import sys


def solution():
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N - 1)]
    print("@", lines)

    end_a, end_b = map(int, input().split())
    if N == 1:
        return min(end_a, end_b)

    prev_a, prev_b = 0, 0
    for i in range(N - 1):
        time_a = min(lines[i][0] + prev_a, lines[i][1] + lines[i][3] + prev_b)
        time_b = min(lines[i][1] + prev_b, lines[i][0] + lines[i][2] + prev_a)
        prev_a = time_a
        prev_b = time_b
        print("@@", time_a, time_b)
    time_a += end_a
    time_b += end_b

    answer = min(time_a, time_b)
    return answer


if __name__ == "__main__":
    print(solution())
