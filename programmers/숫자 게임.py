"""
프로그래머스 : 숫자 게임
"""


def solution(A, B):
    answer = 0

    A = sorted(A, reverse=True)
    B = sorted(B)
    for a in A:
        if a >= B[-1]:
            continue
        else:
            answer += 1
            B.pop()

    return answer


if __name__ == "__main__":
    A = [[5, 1, 3, 7], [2, 2, 2, 2]]
    B = [[2, 2, 6, 8], [1, 1, 1, 1]]
    result = [3, 0]

    for i, data in enumerate(zip(A, B)):
        a, b = data
        print(f"#{i}", solution(a, b))
