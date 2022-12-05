from collections import deque
import copy


def solve():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red = (i, j)
            elif board[i][j] == 'B':
                blue = (i, j)

    visited = [[0 for _ in range(M)] for _ in range(N)]

    """
    구슬 이동함수 (동서남북 방향으로 벽을 만날 때까지 이동, 위치 인덱스와 이동한 횟수를 인자로 받음)
    유의사항
    - red, blue가 인접하고 red-blue로 위치했을 때 왼쪽으로 굴리면 red부터 이동한 후 blue 이동
    - red, blue가 인접하고 blue-red로 위치했을 때 왼쪽으로 굴리면 blue부터 이동한 후 red 이동
        => red와 blue의 위치가 같다면 두 구슬 중 이동거리가 더 긴 구슬이 왔던 방향으로 한 칸 이동(x - dx[i], y - dy[i])
    - board를 기울일 때 마다 board를 갱신해줘야 함 (deepcopy 사용) 
    - red가 goal에 도착하더라도 blue가 뒤이어서 goal에 도착하면 fail
    - blue가 먼저 goal에 도착한다면 fail
    - 움직이는 횟수가 10회를 초과하면 fail
    """

    c_board = copy.deepcopy(board)
    def bfs():
        q = deque()
        q.append((c_board, red, blue, 1)) # c_board : 복제된 보드, red : red 위치, blue : blue 위치, 0 : 기울인 횟수

        while q:
            temp, (rx, ry), (bx, by), count = q.popleft()
            if count > 10:
                print("10 초과")
                return -1

            visited[rx][ry] = 1

            for direction in range(4):
                # r_board = copy.deepcopy(temp)
                # nrx, nry = move(r_board, direction, rx, ry, 'R')
                # b_board = copy.deepcopy(temp)
                # nbx, nby = move(b_board, direction, bx, by, 'B')
                # print(nrx, nry, '/', nbx, nby)

                temp = copy.deepcopy(temp)
                nrx, nry = move(temp, direction, rx, ry, 'R')
                nbx, nby = move(temp, direction, bx, by, 'B')
                # print(temp)

                if visited[nrx][nry] == 1:
                    continue

                if temp[nrx][nry] == 'O' and temp[nbx][nby] != 'O': # blue도 goal에 도착하는지 확인
                    print(temp)
                    return count
                
                print(temp)
                q.append((temp, (nrx, nry), (nbx, nby), count+1))

    answer = bfs()
    if not answer:
        return -1
    return answer

    
def move(board, direction, x, y, color): # board : 보드, direction : 이동 할 방향, i/j : 현재 위치
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        f = is_wall(board, nx, ny)
        if f == 0:              # 더 이상 이동할 수 없다면 x, y 반환
            return (x, y)
        elif f == 2:
            board[x][y] = '.'
            return (nx, ny)
        else:                   # 이동할 수 있다면 이동
            board[x][y] = '.'
            x = nx
            y = ny
            board[x][y] = color


# 구슬이 이동 할 수 있는지 판단 (이동 할 수 없다면 0, 있다면 1, goal이면 2 반환)
def is_wall(board, x, y): # board : 보드, i : 행 index, j : 열 index

    if board[x][y] == '.':
        return 1
    elif board[x][y] == 'O':
        return 2
    elif x >= len(board) or y >= len(board[0]) or x < 0 or y < 0:
        return 0
    else:
        return 0

if __name__ == "__main__":
    print(solve())