"""
https://softeer.ai/practice/6247
[HSAT 7회 정기 코딩 인증평가 기출] 자동차 테스트
"""

import sys


def solution():
    n, q = map(int, input().split())
    fe = list(map(int, input().split()))
    fe = sorted(fe)

    answer = {}
    for i in range(1, n):
        answer[fe[i]] = i * (n - 1 - i)

    for _ in range(q):
        m = int(input())
        # try:
        #     print("#", answer[m])
        # except:
        #     print("#", 0)

        if m in answer:
            print("#", answer[m])
        else:
            print("#", 0)


if __name__ == "__main__":
    solution()
