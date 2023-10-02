"""
프로그래머스 : 최고의 집합
"""


def solution(n, s):
    answer = []

    quotient = s // n  # 몫
    remainder = s % n  # 나머지
    temp = n - remainder  # n - r
    answer = [quotient] * temp + [quotient + 1] * remainder

    if quotient:
        return answer
    return [-1]


if __name__ == "__main__":
    list_n = [2, 2, 2, 2, 3, 4, 5000]
    list_s = [9, 1, 8, 13, 13, 25, 25394]
    result = [[4, 5], [-1], [4, 4]]

    for i, data in enumerate(zip(list_n, list_s)):
        n, s = data
        print(f"#{i}", solution(n, s))
