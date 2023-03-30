def solution():
    n = int(input())
    board1 = [list(input()) for _ in range(n)]
    board2 = [list(input()) for _ in range(n)]

    # for b in board1:
    #     print(b)
    # print()

    answer = [list("." * n) for _ in range(n)]

    # for a in answer:
    #     print(a)
    # print()

    def count_mine(y, x):
        # 상 하 좌 우 왼위 오위 오아래 왼아래
        dy = [-1, 1, 0, 0, -1, -1, 1, 1]
        dx = [0, 0, -1, 1, -1, 1, 1, -1]

        cnt = 0
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if not is_wall(ny, nx) and board1[ny][nx] == "*":
                cnt += 1

        return cnt

    def is_wall(i, j):  # 이동 불가능하면 True, 이동 가능하면 False
        if 0 <= i < n and 0 <= j < n:
            return False
        return True

    flag = 0  # 지뢰가 있는 곳을 골랐다면 1
    mines = []
    for i in range(n):
        for j in range(n):
            if board1[i][j] == "*":  # 지뢰가 있는 위치 저장
                mines.append([i, j])
            if board2[i][j] == "x":
                answer[i][j] = count_mine(i, j)
                if board1[i][j] == "*":  # 확인을 했는데 지뢰가 있는 칸이라면 flag 설정
                    flag = 1

    # 지뢰가 있는 곳 모두 표시
    if flag:
        for i, j in mines:
            answer[i][j] = "*"

    for a in answer:
        print("".join(map(str, a)))


if __name__ == "__main__":
    solution()
