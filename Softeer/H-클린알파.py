"""
https://softeer.ai/practice/6278
H-클린알파
"""

import sys

input = sys.stdin.readline


def solution():
    answer = 0
    P, N = map(int, input().split())
    virus = list(map(int, input().split()))

    def recur(p, n):
        if n <= 1:
            return p
        elif n % 2 == 0:
            result = recur(p, n // 2)
            return (result * result) % 1000000007
        elif n % 2 == 1:
            result = recur(p, n // 2)
            return (result * result * p) % 1000000007

    result = (recur(P, N - 1)) % 1000000007

    for i in range(N):
        answer = (answer + virus[i] * result // P**i) % 1000000007
        print("@", i, answer)

    return answer


if __name__ == "__main__":
    print(solution())
