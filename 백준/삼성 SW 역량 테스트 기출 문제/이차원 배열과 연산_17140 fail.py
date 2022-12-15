def solution():
    answer = 0
    r, c, k = map(int, input().split())
    r = r - 1
    c = c - 1
    A = [list(map(int, input().split())) for _ in range(3)]
    board = [[0] * 100 for _ in range(100)]

    for i in range(len(A)):
        for j in range(len(A[0])):
            board[i][j] = A[i][j]

    # for b in board:
    #     print(b)
    # print()

    time = 0
    while time < 100:
        if board[r][c] == k:
            break

        nr, nc = count_rc(board)
        # print(nr, nc)

        if nr >= nc:  # R연산
            board = sort_row(board)
        else:  # C연산
            board = sort_col(list(zip(*board)))

        # for b in board:
        #     print(b)

        time += 1

    else:
        return -1

    board = sort_row(board)
    for b in board:
        print(b)

    # answer = time
    return answer


def count_rc(board):
    row_num = 0
    col_num = 0

    # column 개수 세기
    for row in range(len(board)):
        if board[row][0] == 0:
            break

        col = 0
        for j in range(len(board[0])):
            if board[row][j] == 0:
                break
            col += 1

        col_num = max(col_num, col)

    # row 개수 세기
    for col in range(len(board[0])):
        if board[0][col] == 0:
            break

        row = 0
        for i in range(len(board[0])):
            if board[i][col] == 0:
                break
            row += 1

        row_num = max(row_num, row)

    return row_num, col_num


def sort_row(board: list):
    for i in range(len(board)):
        nums: dict = {}
        for j in range(len(board[0])):
            if board[i][j]:
                nums.setdefault(board[i][j], 0)
                nums[board[i][j]] += 1
                board[i][j] = 0

        if not nums:
            continue
        # print(nums)
        # print(sorted(nums.items(), key=lambda x: [x[1], x[0]]))

        idx = 0
        for temp in sorted(nums.items(), key=lambda x: [x[1], x[0]]):
            if idx >= 100:
                break
            for t in temp:
                board[i][idx] = t
                idx += 1

    return board


def sort_col(board: list):
    for j in range(len(board[0])):
        nums: dict = {}
        for i in range(len(board)):
            if board[i][j]:
                nums.setdefault(board[i][j], 0)
                nums[board[i][j]] += 1
                board[i][j] = 0

        if not nums:
            continue
        # print(nums)
        # print(sorted(nums.items(), key=lambda x: [x[1], x[0]]))

        idx = 0
        for temp in sorted(nums.items(), key=lambda x: [x[1], x[0]]):
            if idx >= 100:
                break
            for t in temp:
                board[idx][j] = t
                idx += 1

    return board


if __name__ == "__main__":
    print(solution())
