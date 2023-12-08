"""
숫자 카드 나누기
"""
from math import gcd


def solution(arrayA, arrayB):
    answer = 0

    n = len(arrayA)
    gcd1 = 0
    gcd2 = 0
    for i in range(n):
        gcd1 = gcd(gcd1, arrayA[i])
        gcd2 = gcd(gcd2, arrayB[i])
    # print("@", gcd1, gcd2)

    for i in range(n):
        if arrayA[i] % gcd2 == 0:
            gcd2 = 1
        if arrayB[i] % gcd1 == 0:
            gcd1 = 1

    if gcd1 == gcd2 == 1:
        answer = 0
    else:
        answer = max(gcd1, gcd2)

    return answer


if __name__ == "__main__":
    arrayA = [[10, 17], [10, 20], [14, 35, 119], [5, 10, 15], [5, 10, 15, 20]]
    arrayB = [[5, 20], [5, 17], [18, 30, 102], [4, 8, 12], [4, 8, 12, 20]]
    answer = [0, 10, 7]

    for i, data in enumerate(zip(arrayA, arrayB)):
        a, b = data
        print(f"#{i}", solution(a, b))
