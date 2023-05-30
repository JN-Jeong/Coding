def solution():
    N, M, H = map(int, input().split())
    global answer
    answer = 4
    if M == 0:
        return 0

    board = [[0] * (N) for _ in range(H)]

    global line
    line = 1
    for _ in range(M):
        r, c = map(int, input().split())
        board[r - 1][c - 1] = line
        board[r - 1][c] = line
        line += 1

    # for b in board:
    #     print(b)
    # print()

    def check():
        cnt = 0
        for col in range(N):
            c = col
            for r in range(H):
                for d in [1, -1]:
                    nc = c + d
                    if 0 <= nc < N and board[r][c] != 0 and board[r][c] == board[r][nc]:
                        c = nc
                        break

            if c == col:
                cnt += 1
        if cnt == N:
            # for b in board:
            #     print(b)
            # print()
            return True
        return False

    def dfs(cnt):
        global answer, line
        if cnt == 4:
            return

        if check():
            answer = min(answer, cnt)

        for r in range(H):
            for c in range(N - 1):
                if board[r][c] == 0 and board[r][c + 1] == 0:
                    board[r][c] = line
                    board[r][c + 1] = line
                    line += 1
                    dfs(cnt + 1)
                    board[r][c] = 0
                    board[r][c + 1] = 0

    dfs(1)

    if answer > 3:
        return -1
    return answer


if __name__ == "__main__":
    print(solution())
