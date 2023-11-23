"""
2017 팁스타운
예상 대진표
"""


def solution(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
    return answer


if __name__ == "__main__":
    Ns = [8, 8]
    As = [4, 5]
    Bs = [7, 7]
    answer = [3]

    for i, data in enumerate(zip(Ns, As, Bs)):
        n, a, b = data
        print(f"#{i}", solution(n, a, b))
