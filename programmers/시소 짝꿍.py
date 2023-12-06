"""
시소 짝꿍
"""
from collections import Counter


def solution(weights):
    answer = 0

    counter = Counter(weights)
    # 1:1 비율
    for k, v in counter.items():
        if v >= 2:
            answer += v * (v - 1) // 2
    weights = set(weights)
    # print("@", counter, answer)
    # print("@@", weights)

    # 2:3, 2:4, 3:4 비율
    for w in weights:
        if w * 2 / 3 in weights:
            answer += counter[w * 2 / 3] * counter[w]
        if w * 2 / 4 in weights:
            answer += counter[w * 2 / 4] * counter[w]
        if w * 3 / 4 in weights:
            answer += counter[w * 3 / 4] * counter[w]

    return answer


if __name__ == "__main__":
    weights = [[100, 180, 360, 100, 270]]
    answer = [4]

    for i, data in enumerate(weights):
        w = data
        print(f"#{i}", solution(w))
