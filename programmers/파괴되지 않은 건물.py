# def solution(board, skill):
#     answer = 0

#     for t, r1, c1, r2, c2, d in skill:
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 if t == 1:  # 공격
#                     board[r][c] -= d
#                 else:  # 회복
#                     board[r][c] += d

#     for b in board:
#         for n in b:
#             if n > 0:
#                 answer += 1

#     return answer


def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for t, r1, c1, r2, c2, d in skill:
        temp[r1][c1] += d if t == 2 else -d
        temp[r1][c2 + 1] += -d if t == 2 else d
        temp[r2 + 1][c1] += -d if t == 2 else d
        temp[r2 + 1][c2 + 1] += d if t == 2 else -d

    for t in temp:
        print(t)
    print()

    # 가로로 복원
    for i in range(len(temp) - 1):
        for j in range(len(temp[0]) - 1):
            temp[i][j + 1] += temp[i][j]

    # 세로로 복원
    for j in range(len(temp[0]) - 1):
        for i in range(len(temp) - 1):
            temp[i + 1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1

    for b in board:
        print(b)

    return answer


if __name__ == "__main__":
    board = [
        [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    ]
    skill = [
        [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]],
        [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
    ]
    result = [10, 6]
    for b, s in zip(board, skill):
        print(solution(b, s))
