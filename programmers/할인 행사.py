"""
할인 행사
"""


def solution(want, number, discount):
    answer = 0

    wants = {}
    for w, n in zip(want, number):
        wants.setdefault(w, n)

    n = sum(number)
    for i in range(len(discount) - n + 1):
        temp = wants.copy()
        for j in range(i, i + n):
            if discount[j] in temp:
                temp[discount[j]] -= 1

        flag = True
        for v in temp.values():
            if v > 0:
                flag = False
                break

        if flag:
            answer += 1

    return answer


if __name__ == "__main__":
    wants = [["banana", "apple", "rice", "pork", "pot"], ["apple"]]
    numbers = [[3, 2, 2, 2, 1], [10]]
    discounts = [
        [
            "chicken",
            "apple",
            "apple",
            "banana",
            "rice",
            "apple",
            "pork",
            "banana",
            "pork",
            "rice",
            "pot",
            "banana",
            "apple",
            "banana",
        ],
        [
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
            "banana",
        ],
    ]

    answer = [3, 0]

    for i, data in enumerate(zip(wants, numbers, discounts)):
        w, n, d = data
        print(f"#{i}", solution(w, n, d))
