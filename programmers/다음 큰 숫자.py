"""
프로그래머스 : 다음 큰 숫자
"""


def solution(n):
    one = int(str(bin(n)).count("1"))
    for i in range(n + 1, 1000001):
        temp = int(str(bin(i).count("1")))
        if temp == one:
            return i


if __name__ == "__main__":
    ns = [78, 15]
    result = [83, 23]

    for i, data in enumerate(ns):
        n = data
        print(f"#{i}", solution(n))
