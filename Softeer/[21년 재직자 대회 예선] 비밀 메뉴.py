"""
https://softeer.ai/practice/6269
[21년 재직자 대회 예선] 비밀 메뉴
"""

import sys


def solution():
    m, n, k = map(int, input().split())
    secret = list(map(int, input().split()))
    buttons = list(map(int, input().split()))

    if len(buttons) < len(secret):
        return "normal"

    for i in range(len(buttons) - len(secret) + 1):
        if buttons[i] == secret[0]:
            for j in range(len(secret)):
                if buttons[i + j] != secret[j]:
                    break
            else:
                return "secret"

    return "normal"


if __name__ == "__main__":
    print(solution())
