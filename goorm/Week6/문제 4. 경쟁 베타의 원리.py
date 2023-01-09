# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# def solution():
#     answer = 0
#     N, K = map(int, input().split())
#     habitats = [list(map(int, input().split())) for _ in range(N)]

#     max_ = 0
#     for h in habitats:
#         max_ = max(max_, max(h))

#     board = [[0] * (max_) for _ in range(max_)]

#     for x1, y1, x2, y2 in habitats:
#         for row in range(x1, x2):
#             for col in range(y1, y2):
#                 board[row][col] += 1

#     for b in board:
#         answer += b.count(K)

#     return answer


def solution():
    N, K = map(int, input().split())
    L = 1004
    answer = 0

    S = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        S[y1][x1] += 1
        S[y1][x2] -= 1
        S[y2][x1] -= 1
        S[y2][x2] += 1

    # 가로로 복원
    for i in range(L):
        for j in range(1, L):
            S[i][j] += S[i][j - 1]

    # 세로로 복원
    for j in range(L):
        for i in range(1, L):
            S[i][j] += S[i - 1][j]

    for i in range(L):
        for j in range(L):
            if S[i][j] == K:
                answer += 1

    return answer


if __name__ == "__main__":
    print(solution())


"""
3 2
1 1 5 5
4 4 7 6
3 3 8 7
"""
