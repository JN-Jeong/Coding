# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from itertools import permutations


def solution():
    answer = float("inf")

    N = int(input())
    cards = list(map(int, input().split()))
    cards = sorted(cards)

    for permu in permutations(cards, N):
        temp = permu[0]
        for i in range(1, N):
            if temp % 10 == permu[i] // 10:
                temp = temp * 10 + permu[i] % 10
            else:
                temp = temp * 100 + permu[i]
        answer = min(answer, temp)

    return answer


if __name__ == "__main__":
    print(solution())

"""
4
42 31 16 19 : 1631942

4
16 19 42 91 : 1619142

4
14 18 42 81 : 142181

9
14 18 41 42 43 44 81 82 83 -> 14 41 18 81 43 44 42 82 83 : 14181434428283

10
14 18 41 42 43 44 81 82 83 84 -> 14 41 18 81 44 42 82 83 84 42 : 14181434428283842

11
14 18 41 42 43 44 51 81 82 83 84 85 -> 14 41 18 81 44 42 82 83 84 43 85 51  : 14181434428283842851

4
14 23 33 42 -> 14 42 23 33 : 14233

2
32 43 -> 43 32 : 432

2
87 88 -> 88 87 : 887

3
52 53 65 -> 53 65 52 : 52653
"""
