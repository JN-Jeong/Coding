"""
행렬의 곱셈
"""


def solution(arr1, arr2):
    row1 = len(arr1)
    col1 = len(arr1[0])
    row2 = len(arr2)
    col2 = len(arr2[0])

    row = row1
    col = col2
    answer = [[0] * col for _ in range(row)]

    for y in range(row):
        for x in range(col):
            result = 0
            for i in range(col1):
                result += arr1[y][i] * arr2[i][x]
            answer[y][x] = result

    return answer


if __name__ == "__main__":
    arr1 = [[[1, 4], [3, 2], [4, 1]], [[2, 3, 2], [4, 2, 4], [3, 1, 4]]]
    arr2 = [[[3, 3], [3, 3]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]]

    answer = [
        [[15, 15], [15, 15], [15, 15]],
        [[22, 22, 11], [36, 28, 18], [29, 20, 14]],
    ]

    for i, data in enumerate(zip(arr1, arr2)):
        a1, a2 = data
        print(f"#{i}", solution(a1, a2))
