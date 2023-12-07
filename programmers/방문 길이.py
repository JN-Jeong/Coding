"""
Summer/Winter Coding(~2018)
방문 길이
"""


def solution(dirs):
    answer = 0

    board = [[0] * 21 for _ in range(21)]  # 이동한 경로를 포함하기 위해 board 크기를 2배로 늘림
    # for b in board:
    #     print(b)
    # print()

    # 상좌하우
    directs = {"U": 0, "L": 1, "D": 2, "R": 3}
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    def isin(y, x):
        if 0 <= y < 21 and 0 <= x < 21:
            return True
        return False

    y = 10
    x = 10
    for d in dirs:
        ny = y + dy[directs[d]]
        nx = x + dx[directs[d]]

        if isin(ny, nx):
            # 이동한 경로(선)는 짝수 좌표로 체크
            if board[ny][nx] == 0:
                answer += 1
            board[ny][nx] = 1
            # 위치(점)는 홀수 좌표로 체크
            y = ny + dy[directs[d]]
            x = nx + dx[directs[d]]

    # for b in board:
    #     print(b)
    # print()

    return answer


if __name__ == "__main__":
    dirs = ["ULURRDLLU", "LULLLLLLU", "LLLLLLLRRRRRR"]

    answer = [7, 7]

    for i, data in enumerate(dirs):
        d = data
        print(f"#{i}", solution(d))
