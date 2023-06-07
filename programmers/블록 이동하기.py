from collections import deque


def solution(board):
    answer = 0
    N = len(board)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    q = deque()
    q.append(([0, 0], [0, 1], 0))
    visited = [[[[0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]  # visited[r1][c1][r2][c2]: 로봇 2칸 방문 기록
    visited[0][0][0][1] = 1

    while q:
        (r1, c1), (r2, c2), cnt = q.popleft()
        if (r1 == N - 1 and c1 == N - 1) or (r2 == N - 1 and c2 == N - 1):
            return cnt

        for d in range(4):
            nrow1 = r1 + dy[d]
            ncol1 = c1 + dx[d]
            nrow2 = r2 + dy[d]
            ncol2 = c2 + dx[d]

            if 0 <= nrow1 < N and 0 <= nrow2 < N and 0 <= ncol1 < N and 0 <= ncol2 < N and visited[nrow1][ncol1][nrow2][ncol2] == 0:
                if board[nrow1][ncol1] == 1 or board[nrow2][ncol2] == 1:
                    continue
                visited[nrow1][ncol1][nrow2][ncol2] == 1
                q.append(([nrow1, ncol1], [nrow2, ncol2], cnt + 1))

        if r1 == r2:  # 로봇이 가로일 때
            for d in [-1, 1]:
                nrow1 = r2 + d
                ncol1 = c2
                nrow2 = r1 + d
                ncol2 = c1
                if 0 <= nrow1 < N and 0 <= nrow2 < N and visited[r1][c1][nrow2][ncol2] == 0 and visited[nrow1][ncol1][r2][c2] == 0:
                    if board[nrow1][ncol1] == 1 or board[nrow2][ncol2] == 1:
                        continue
                    visited[r1][c1][nrow2][ncol2] = 1
                    visited[nrow1][ncol1][r2][c2] = 1
                    q.append(([r1, c1], [nrow2, ncol2], cnt + 1))  # 1번 로봇 기준
                    q.append(([nrow1, ncol1], [r2, c2], cnt + 1))  # 2번 로봇 기준

        elif c1 == c2:  # 로봇이 세로일 때
            for d in [-1, 1]:
                nrow1 = r2
                ncol1 = c2 + d
                nrow2 = r1
                ncol2 = c1 + d
                if 0 <= ncol1 < N and 0 <= ncol2 < N and visited[r1][c1][nrow2][ncol2] == 0 and visited[nrow1][ncol1][r2][c2] == 0:
                    if board[nrow1][ncol1] == 1 or board[nrow2][ncol2] == 1:
                        continue
                    visited[r1][c1][nrow2][ncol2] = 1
                    visited[nrow1][ncol1][r2][c2] = 1
                    q.append(([r1, c1], [nrow2, ncol2], cnt + 1))  # 1번 로봇 기준
                    q.append(([nrow1, ncol1], [r2, c2], cnt + 1))  # 2번 로봇 기준

    return answer


if __name__ == "__main__":
    board = [[[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]]
    result = [7]
    for b in board:
        print(solution(b))


"""
상하좌우
(0,0), (0,1) -> (-1,0), (-1,1)
(0,0), (0,1) -> (1,0), (1,1)
(0,0), (0,1) -> (0,-1), (0,0)
(0,0), (0,1) -> (0,1), (0,2)

가로일 때 좌우 회전
(r1,c1), (r2,c2) -> 한 쪽 column 기준으로 row가 -1, 1 이동
세로일 때 좌우 회전
(r1,c1), (r2,c2) -> 한 쪽 row 기준으로 column이 -1, 1 이동

1 기준 좌우 회전 (가로)
(r1,c1), (r2,c2) -> (r1,c1), (r1-1,c1)/(r1+1,c1)
(0,0), (0,1) -> (0,0), (-1,0)
(0,0), (0,1) -> (0,0), (1,0)

2 기준 좌우 회전 (가로)
(r1,c1), (r2,c2) -> (r2-1,c2)/(r2+1,c2), (r2,c2)
(0,0), (0,1) -> (1,1), (0,1)
(0,0), (0,1) -> (-1,1), (0,1)

상하좌우
(0,0), (1,0) -> (-1,0), (0,0)
(0,0), (1,0) -> (1,0), (2,0)
(0,0), (1,0) -> (0,-1), (1,-1)
(0,0), (1,0) -> (0,1), (1,1)

1 기준 좌우 회전 (세로)
(r1,c1), (r2,c2) -> (r1,c1), (r1,c1-1)/(r1,c1+1)
(0,0), (1,0) -> (0,0), (0,-1)
(0,0), (1,0) -> (0,0), (0,1)

2 기준 좌우 회전 (세로)
(r1,c1), (r2,c2) -> (r2,c2-1)/(r2,c2+1), (r2,c2)
(0,0), (1,0) -> (0,-1), (1,0)
(0,0), (1,0) -> (0,1), (1,0)
"""
