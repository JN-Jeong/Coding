"""
땅따먹기
"""


def solution(land):
    answer = 0

    N = len(land)
    for i in range(1, N):
        for j in range(4):
            result = 0
            for col in range(4):
                if j != col:
                    result = max(result, land[i][j] + land[i - 1][col])
            land[i][j] = result
    print("@", land)
    answer = max(land[-1])
    return answer


if __name__ == "__main__":
    lands = [[[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]]

    answer = [16]

    for i, data in enumerate(lands):
        s = data
        print(f"#{i}", solution(s))
