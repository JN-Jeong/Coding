def solution(board, aloc, bloc):
    answer = -1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def in_range(board, y, x):
        if 0 <= y < len(board) and 0 <= x < len(board[0]):
            return True
        else:
            return False

    def is_finished(board, y, x):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if in_range(board, ny, nx) and board[ny][nx]:
                return False
        return True

    def dfs(board, y1, x1, y2, x2):
        if is_finished(board, y1, x1):
            return [False, 0]

        if y1 == y2 and x1 == x2:  # 서로 위치가 같을 때 이번 턴에 움직이면 승리
            return [True, 1]

        min_turn = float("inf")
        max_turn = 0
        can_win = False

        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if not in_range(board, ny, nx) or not board[ny][nx]:
                continue

            board[y1][x1] = 0
            result = dfs(board, y2, x2, ny, nx)
            board[y2][x2] = 1

            if not result[0]:
                can_win = True
                min_turn = min(min_turn, result[1])
            elif not can_win:
                max_turn = max(max_turn, result[1])

        turn = min_turn if can_win else max_turn

        return [can_win, turn + 1]

    return dfs(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]


if __name__ == "__main__":
    board = [
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1, 1, 1]],
        [[1]],
    ]
    aloc = [
        [1, 0],
        [1, 0],
        [0, 0],
        [0, 0],
    ]
    bloc = [
        [1, 2],
        [1, 2],
        [0, 4],
        [0, 0],
    ]
    result = [5, 4, 4, 0]

    for b, al, bl in zip(board, aloc, bloc):
        print(solution(b, al, bl))
