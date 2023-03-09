def solution():
    N, M = map(int, input().split())
    arr = [[0] * (M + 1) if i == 0 else [0] + list(map(int, input().split())) for i in range(N + 1)]

    K = int(input())

    sum_arr = arr.copy()
    # 가로
    for i in range(N + 1):
        for j in range(1, M):
            sum_arr[i][j + 1] += sum_arr[i][j]
    # 세로
    for j in range(M + 1):
        for i in range(1, N):
            sum_arr[i + 1][j] += sum_arr[i][j]

    # for a in sum_arr:
    #     print(a)

    for _ in range(K):
        i, j, x, y = map(int, input().split())
        i, j = i - 1, j - 1
        print(sum_arr[x][y] - (sum_arr[i][y] + sum_arr[x][j]) + sum_arr[i][j])


if __name__ == "__main__":
    solution()
