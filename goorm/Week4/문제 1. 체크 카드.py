# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    N, M = map(int, input().split())
    answer = N
    waitings = []

    for _ in range(M):
        transaction, money = input().split()
        money = int(money)
        if transaction == "deposit":
            answer += money
        elif transaction == "pay":
            if answer >= money:
                answer -= money
        elif transaction == "reservation":
            waitings.append(money)

        while waitings and answer >= waitings[0]:
            answer -= waitings.pop(0)

        # print(answer, waitings)

    return answer


if __name__ == "__main__":
    print(solution())
