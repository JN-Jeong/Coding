# dfs로 해결 가능
from itertools import combinations


def solution():
    answer = float("inf")
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    chickens = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                chickens.append((i, j))
                board[i][j] = 0

    print(chickens)
    print(list(combinations(range(len(chickens)), M)))

    for ids in list(combinations(range(len(chickens)), M)):
        for idx in ids:
            board[chickens[idx][0]][chickens[idx][1]] = 2
        for b in board:
            print(b)
        print()

        total = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    dis = chicken_distance(board, i, j)
                    total += dis

        answer = min(answer, total)

        for idx in ids:
            board[chickens[idx][0]][chickens[idx][1]] = 0

    return answer


# 치킨 거리 구하는 메서드
def chicken_distance(board: list, row: int, col: int):  # row, col : 집의 위치
    dis = 100
    n = len(board)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                dis = min(dis, abs(row - i) + abs(col - j))  # 치킨집과 집의 거리 갱신

    return dis  # 치킨 거리 반환


if __name__ == "__main__":
    print(solution())
