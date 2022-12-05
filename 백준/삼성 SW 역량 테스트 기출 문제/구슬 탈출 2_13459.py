from collections import deque


def solve():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red = (i, j)
            elif board[i][j] == 'B':
                blue = (i, j)

    # 상하좌우 탐색
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    """
    구슬 이동함수 (동서남북 방향으로 벽을 만날 때까지 이동, 위치 인덱스와 이동한 횟수를 인자로 받음)
    유의사항
    - red, blue가 인접하고 red-blue로 위치했을 때 왼쪽으로 굴리면 red부터 이동한 후 blue 이동
    - red, blue가 인접하고 blue-red로 위치했을 때 왼쪽으로 굴리면 blue부터 이동한 후 red 이동
        => red와 blue의 위치가 같다면 두 구슬 중 이동거리가 더 긴 구슬이 왔던 방향으로 한 칸 이동(x - dx[i], y - dy[i])
    - board를 기울일 때 마다 board를 갱신해줘야 함 (deepcopy 사용) (필요없음)
    - red가 goal에 도착하더라도 blue가 뒤이어서 goal에 도착하면 fail
    - blue가 먼저 goal에 도착한다면 fail
    - 움직이는 횟수가 10회를 초과하면 fail
    """

    visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]  # [red_x][red_y][blue_x][blue_y]
    def bfs():
        q = deque() # -> q = list()
        q.append((red, blue, 1)) # red : red 위치, blue : blue 위치, 1 : 기울인 횟수
        print(red, '/', blue)

        while q:
            (rx, ry), (bx, by), count = q.popleft() # -> q.pop(0)
            if count > 10:
                # print("10 초과")
                return -1

            for direction in range(4): # 상하좌우 탐색
                nrx, nry, rd = move(direction, rx, ry)
                nbx, nby, bd = move(direction, bx, by)
                print(nrx, nry, '/', nbx, nby)

                if board[nbx][nby] == 'O': # blue가 goal에 도착하면 continue
                    continue

                if board[nrx][nry] == 'O': 
                    # print(nrx, nry, '/', nbx, nby)
                    return count

                if nrx == nbx and nry == nby: # 구슬이 겹쳤을 때 겹치지 않도록 위치 갱신
                    if rd > bd:
                        nrx = nrx - dx[direction]
                        nry = nry - dy[direction]
                    else:
                        nbx = nbx - dx[direction]
                        nby = nby - dy[direction]

                if visited[nrx][nry][nbx][nby] == 1:
                    continue
                
                visited[rx][ry][bx][by] = 1
                # print(visited)
                q.append(((nrx, nry), (nbx, nby), count+1))

    # 구슬 움직이기
    def move(direction, x, y): # direction : 이동 할 방향, i/j : 현재 위치, dis : 이동한 거리
        # dx = [1,-1,0,0]
        # dy = [0,0,1,-1]
        dis = 0
        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]
            dis += 1

            f = is_wall(nx, ny)
            if f == 0:              # 더 이상 이동할 수 없다면 x, y 반환
                return (x, y, dis)
            elif f == 2:
                return (nx, ny, dis)
            else:                   # 이동할 수 있다면 이동
                x = nx
                y = ny

    # 구슬이 이동 할 수 있는지 판단 (이동 할 수 없다면 0, 있다면 1, goal이면 2 반환)
    def is_wall(x, y): # i : 행 index, j : 열 index

        if board[x][y] == 'O':
            return 2
        elif x >= len(board) or y >= len(board[0]) or x < 0 or y < 0 or board[x][y] == '#':
            return 0
        else:
            return 1

    answer = bfs()
    if not answer:
        return -1
    return answer
    
    
if __name__ == "__main__":
    print(solve())