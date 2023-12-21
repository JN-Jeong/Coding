"""
https://softeer.ai/practice/6279
스마트 물류
"""

import sys


def solution():
    N, K = map(int, input().split())
    robots = list(input())

    left_robots = robots[:]
    right_robots = robots[:]
    answer = 0
    left, right = 0, 0
    for i in range(N):
        if robots[i] == "P":
            # left
            for j in range(-K, K + 1):
                if 0 <= i + j < N and left_robots[i + j] == "H":
                    left_robots[i + j] = ""
                    left += 1
                    break

            # right
            for j in range(K, -K - 1, -1):
                if 0 <= i + j < N and right_robots[i + j] == "H":
                    right_robots[i + j] = ""
                    right += 1
                    break

    # print("@", left_robots)
    # print("#", right_robots)
    answer = max(left, right)
    return answer


if __name__ == "__main__":
    print(solution())
