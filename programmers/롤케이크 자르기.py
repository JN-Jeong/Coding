"""
롤케이크 자르기
"""
from collections import Counter


def solution(topping):
    answer = 0

    total = len(set(topping))
    lefts = {}
    left = 0
    rights = Counter(topping)
    right = total
    for i in range(len(topping) - 1):
        if rights[topping[i]] > 0:
            rights[topping[i]] -= 1
            if rights[topping[i]] == 0:
                right -= 1

        if topping[i] not in lefts:
            lefts[topping[i]] = 1
            left += 1

        if right == left:
            answer += 1
        # print("@", left, right)

    return answer


if __name__ == "__main__":
    toppings = [[1, 2, 1, 3, 1, 4, 1, 2], [1, 2, 3, 1, 4]]
    answer = [2, 0]

    for i, data in enumerate(toppings):
        t = data
        print(f"#{i}", solution(t))
