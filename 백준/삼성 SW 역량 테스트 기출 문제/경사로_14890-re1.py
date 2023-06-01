def solution():
    N, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    def solve(arr):
        used = [0] * N
        for j in range(1, N):
            if abs(arr[j - 1] - arr[j]) > 1:  # 높이 차이가 1보다 크면 설치 못함
                return False

            if arr[j - 1] < arr[j]:  # 왼쪽 방향으로 확인
                for k in range(L):  # 경사로 길이만큼 확인
                    # 1. 범위를 벗어나거나 2. 이미 경사로가 설치되었거나 3. 연속된 칸의 높이가 다르다면 설치 못함
                    if j - 1 - k < 0 or used[j - 1 - k] == 1 or arr[j - 1] != arr[j - 1 - k]:
                        return False
                    used[j - 1 - k] = 1

            elif arr[j - 1] > arr[j]:  # 오른쪽 방향으로 확인
                for k in range(L):  # 경사로 길이만큼 확인
                    # 1. 범위를 벗어나거나 2. 이미 경사로가 설치되었거나 3. 연속된 칸의 높이가 다르다면 설치 못함
                    if j + k >= N or used[j + k] == 1 or arr[j] != arr[j + k]:
                        return False
                    used[j + k] = 1

            # print(used)

        return True

    answer = 0
    # 행
    for i in range(N):
        if solve(board[i]):
            answer += 1
    # 열
    for j in range(N):
        if solve([board[i][j] for i in range(N)]):
            answer += 1

    print(answer)


if __name__ == "__main__":
    solution()
