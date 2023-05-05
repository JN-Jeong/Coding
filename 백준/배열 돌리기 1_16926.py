import math


def solution():
    N, M, R = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(R):
        for i in range(math.ceil(min(N, M) / 2)):
            # for i in range(3):
            n = N - 1 - i
            m = M - 1 - i
            start = 0 + i
            temp = array[n][start]
            # print(temp)

            # 아래
            for x in range(start + 1, m + 1):
                array[n][x], temp = temp, array[n][x]
            # print(temp)

            # 오른쪽
            for y in range(n - 1, start - 1, -1):
                array[y][m], temp = temp, array[y][m]
            # print(temp)

            # 위
            for x in range(m - 1, start - 1, -1):
                array[start][x], temp = temp, array[start][x]
            # print(temp)

            # 왼쪽
            for y in range(start + 1, n + 1):
                array[y][start], temp = temp, array[y][start]
            # print(temp)

    for a in array:
        print(*a)
    # print(temp)


if __name__ == "__main__":
    solution()
