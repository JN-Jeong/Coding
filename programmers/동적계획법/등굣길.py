def solution(m, n, puddles):
    answer = 0

    board = make_board(m, n)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles: #
                board[i][j] = 0
            else:
                board[i][j] = (board[i-1][j] + board[i][j-1])
    
    # for b in board:
    #     print(b)

    answer = board[n][m] % 1000000007
    return answer

def make_board(row, col):
    board = [[0] * (row + 1) for _ in range(col + 1)]
    board[1][1] = 1

    return board

m_ = [4]
n_ = [3]
puddles = [[[2, 2]]	, ]

for m, n, puddle in zip(m_, n_, puddles):
    print(solution(m, n, puddle))