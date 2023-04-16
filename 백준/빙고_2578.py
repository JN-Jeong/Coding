from copy import deepcopy


def solution():
    board = [list(map(int, input().split())) for _ in range(5)]
    bingo = deepcopy(board)

    nums = []
    for _ in range(5):
        nums += list(map(int, input().split()))

    for idx, n in enumerate(nums):
        for i in range(5):
            for j in range(5):
                if board[i][j] == n:
                    bingo[i][j] = 1
                    if is_bingo(bingo):
                        return idx + 1


def is_bingo(bingo):
    line = 0
    # 가로줄
    for i in range(5):
        if sum(bingo[i]) == 5:
            line += 1

    # 세로줄
    for i in range(5):
        if sum(list(zip(*bingo))[i]) == 5:
            line += 1

    # 대각선
    left_diagonal = 0
    right_diagonal = 0
    for i in range(5):
        left_diagonal += bingo[i][i]
        right_diagonal += bingo[i][4 - i]

    if left_diagonal == 5:
        line += 1
    if right_diagonal == 5:
        line += 1

    if line >= 3:
        return True
    return False


if __name__ == "__main__":
    print(solution())
