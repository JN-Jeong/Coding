from copy import deepcopy


def solution():
    T = int(input())

    def rot45(array, N, d):
        temp = deepcopy(array)

        for _ in range(d):
            # 가로줄
            for i in range(N):
                temp[i][i] = array[N // 2][i]

            # 세로줄
            for i in range(N):
                temp[i][N - i - 1] = array[i][N // 2]

            # 주 대각선
            for i in range(N):
                temp[i][N // 2] = array[i][i]

            # 부 대각선
            for i in range(N):
                temp[N // 2][N - i - 1] = array[i][N - i - 1]

            array = deepcopy(temp)

        return temp

    for _ in range(T):
        n, d = map(int, input().split())
        array = [list(map(int, input().split())) for _ in range(n)]

        d = ((360 + d) // 45) % 8
        for a in rot45(array, n, d):
            print(*a)


if __name__ == "__main__":
    solution()
