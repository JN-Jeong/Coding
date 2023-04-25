def solution():
    N = int(input())
    board = [[0] * 100 for _ in range(100)]

    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]

    def curve(y, x, gen, directions):
        ny = y
        nx = x

        for g in range(gen + 1):
            result = []
            mid = len(directions) // 2

            if g == 0:
                for d in directions:
                    nd = d
                    ny = y + dy[nd]
                    nx = x + dx[nd]
                    if 0 <= ny < 100 and 0 <= nx < 100:
                        board[ny][nx] = 1

            elif g == 1:
                for d in directions:
                    nd = (d + 1) % 4
                    ny = ny + dy[nd]
                    nx = nx + dx[nd]
                    if 0 <= ny < 100 and 0 <= nx < 100:
                        board[ny][nx] = 1
                    result.append(nd)

            else:
                for d in directions[:mid]:
                    nd = (d + 2) % 4
                    ny = ny + dy[nd]
                    nx = nx + dx[nd]
                    if 0 <= ny < 100 and 0 <= nx < 100:
                        board[ny][nx] = 1
                    result.append(nd)

                for d in directions[mid:]:
                    nd = d
                    ny = ny + dy[nd]
                    nx = nx + dx[nd]
                    if 0 <= ny < 100 and 0 <= nx < 100:
                        board[ny][nx] = 1
                    result.append(nd)

            directions.extend(result)

        return directions

    for _ in range(N):
        x, y, d, g = map(int, input().split())
        board[y][x] = 1
        curve(y, x, g, [d])

    # print()
    # for b in board:
    #     print(b)
    # print()

    answer = 0
    for r in range(len(board) - 1):
        for c in range(len(board[0]) - 1):
            if board[r][c] == 1 and board[r + 1][c] == 1 and board[r][c + 1] == 1 and board[r + 1][c + 1] == 1:
                answer += 1

    return answer


if __name__ == "__main__":
    print(solution())


"""
시계방향 90도 회전
우 -> 하
상 -> 우
좌 -> 상
하 -> 좌

반대
우 -> 좌
상 -> 하
좌 -> 우
하 -> 상

시계방향 90도 회전 + 반대
우 (0) -> 상 (1)
상 (1) -> 좌 (2)
좌 (2) -> 하 (3)
하 (3) -> 우 (0)


새로운 드래곤 커브
기존 커브 + 기존 커브 마지막 지점부터 기존 커브의 시계방향 90도 회전한 좌표의 순서와 방향을 반대로 추가


시작 방향 : 우
0세대
0, 0 -> 0, 1 (우)

1세대
0, 1 -> 0, 1
0, 0 -> -1, 1 (상)

2세대
-1, 1 -> -1, 1
0, 1 -> -1, 0 (좌)
0, 0 -> -2, 0 (상)

3세대
-2, 0 -> -2, 0
-1, 0 -> -2, -1 (좌)
-1, 1 -> -1, -1 (하)
0, 1 -> -1, -2 (좌)
0, 0 -> -2, -2 (상)

4세대
-2, -2 -> -2, -2
-1, -2 -> -2, -3 (좌)
-1, -1 -> -1, -3 (하)
-2, -1 -> -1, -2 (우)
-2, 0 -> 0, -2 (하)
-1, 0 -> 0, -3 (좌)
-1, 1 -> 1, -3 (하)
0, 1 -> 1, -4 (좌)
0, 0 -> 0, -4 (상)

우 -> 상
우 상 -> 좌 상
우상 좌상 -> 좌하 좌상
우상좌상 좌하좌상 -> 좌하우하 좌하좌상



시작 방향 : 하
0세대
0, 0 -> 1, 0 (하)

1세대
1, 0 -> 1, 0
0, 0 -> 1, 1 (우)

2세대
1, 1 -> 1, 1
1, 0 -> 0, 1 (상)
0, 0 -> 0, 2 (우)

3세대
0, 2 -> 0, 2
0, 1 -> -1, 2 (상)
1, 1 -> -1, 1 (좌)
1, 0 -> -2, 1 (상)
0, 0 -> -2, 2 (우)

4세대
-2, 2 -> -2, 2
-2, 1 -> -3, 2 (상)
-1, 1 -> -3, 1 (좌)
-1, -2 -> -2, 1 (하)
0, 2 -> -2, 0 (좌)
0, 1 -> -3, 0 (상)
1, 1 -> -3, -1 (좌)
1, 0 -> -4, -1 (상)
0, 0 -> -4, 0 (우)

하 -> 우
하 우 -> 상 우
하우 상우 -> 상좌 상우
하우상우 상좌상우 -> 상좌하좌 상좌상우
"""
