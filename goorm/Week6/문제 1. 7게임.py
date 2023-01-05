# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    answer = []

    for _ in range(5):
        result = 0
        K = input()
        for i in range(0, len(K), 2):
            result += int(K[i])

        for i in range(1, len(K), 2):
            if int(K[i]) != 0:
                result *= int(K[i])

        result %= 10
        answer.append(result)

    return answer


if __name__ == "__main__":
    for s in solution():
        print(s)
