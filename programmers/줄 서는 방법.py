"""
줄 서는 방법
"""
import math


def solution(n, k):
    answer = []
    arr = [i for i in range(1, n + 1)]
    # print(temp)

    while arr:
        result = (k - 1) // math.factorial(n - 1)
        # print("@", k, result)
        answer.append(arr.pop(result))

        k = k % math.factorial(n - 1)
        n -= 1
        # print("@@", temp, k, answer)

    return answer


if __name__ == "__main__":
    ns = [3]
    ks = [5]
    answer = [[3, 1, 2]]

    for i, data in enumerate(zip(ns, ks)):
        n, k = data
        print(f"#{i}", solution(n, k))
