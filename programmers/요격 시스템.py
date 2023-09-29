"""
프로그래머스 : 요격 시스템
"""


def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x: x[1])

    idx = -1
    for i in range(len(targets)):
        if idx < targets[i][0]:
            answer += 1
            idx = targets[i][1] - 0.00001

    return answer


if __name__ == "__main__":
    targets = [
        [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]],
        [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7]],
        [[4, 5], [4, 8], [3, 7], [1, 5]],
    ]
    result = [3, 2]

    for i, data in enumerate(targets):
        t = data
        print(f"#{i}", solution(t))
