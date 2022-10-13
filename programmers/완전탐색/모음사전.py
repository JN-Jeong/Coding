from itertools import product


def solution(word):
    answer = 0
    alphabets = ["A", "E", "I", "O", "U"]
    result = []
    for i in range(1, 6):
        for c in product(alphabets, repeat=i):
            result.append("".join(list(c)))

    print(result)
    print(sorted(result))

    return sorted(result).index(word) + 1


words = ["AAAAE", "AAAE", "I", "EIO"]
result = [6, 10, 1563, 1189]

for word in words:
    print(solution(word))
