def solve():
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    return bfs(maze)
        
def bfs(maze):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    loc = []

    N = len(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                loc.append((i, j)) # 출발 위치
                break

    visited_bfs = [[0] * N for _ in range(N)]
    while loc:
        x, y = loc.pop()
        visited_bfs[x][y] = 1

        for i in range(4):
            loc_x = x + dx[i]
            loc_y = y + dy[i]

            if wall_chk(loc_x, loc_y, maze) and visited_bfs[loc_x][loc_y] == 0: # 미로를 벗어나지 않고 통로라면
                loc.append((loc_x, loc_y))
                visited_bfs[loc_x][loc_y] = 1
                if maze[loc_x][loc_y] == '3':
                    return 1
    return 0

def wall_chk(x, y, maze):
    N = len(maze)
    if 0 <= x < N and 0 <= y < N and maze[x][y] != '1': # 미로를 벗어나지 않고 통로인 경우 return 1
        return 1
    else:
        return 0

if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))
