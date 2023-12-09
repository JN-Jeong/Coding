"""
N개의 최소공배수
"""
from math import gcd


def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        answer = int((arr[i] * answer) / gcd(arr[i], answer))
        print("@", answer)

    return answer


if __name__ == "__main__":
    arr = [[2, 6, 8, 14], [1, 2, 3]]
    answer = [168, 6]

    for i, data in enumerate(arr):
        a = data
        print(f"#{i}", solution(a))
