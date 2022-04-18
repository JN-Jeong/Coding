def solve():
    N = int(input())

    global maze
    maze = [list(input()) for _ in range(N)]

    print(maze)

    global min_path
    min_path = len(maze) * len(maze[0]) + 1

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "2":
                # start = [(i, j, min_path)]
                start = (i, j, 0)

    print(start)
    
    visited_maze = [[0] * len(maze) for _ in range(len(maze[0]))]

    # return bfs(start)

    dfs(start, visited_maze)
    return min_path


def is_path(loc): # 통로이면 True 반환, 아니면 False 반환
    global maze
    x, y = loc
    if x >= len(maze[0]) or y >= len(maze) or maze[x][y] == "1":
        return False
    else:
        return True


def bfs(loc):
    global maze
    global min_path
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited_maze = [[0] * len(maze) for _ in range(len(maze[0]))]

    while loc:
        start_x, start_y = loc.pop()
        visited_maze[start_x][start_y] = 1

        for i in range(4):
            x = start_x + dx[i]
            y = start_y + dy[i]

            if is_path((x,y)) and visited_maze[x][y] == 0:
                loc.append((x,y))
                visited_maze[x][y] = 1
                # print("미로 : ", maze)
                print(x, y)
                min_path += 1
                if maze[x][y] == "3": # 도착했다면 경로 칸 수 반환
                    return min_path
        print(visited_maze)
    return 0


def dfs(loc, visited_maze):
    global min_path
    
    pre_x, pre_y, path = loc
    visited_maze[pre_x][pre_y] = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        x = pre_x + dx[i]
        y = pre_y + dy[i]

        if is_path((x,y)) and visited_maze[x][y] == 0:
            if maze[x][y] == "3":
                print("도착 발견", path)
                visited_maze[x][y] = 1
                print("v maze 3 : ", visited_maze)
                if min_path > path:
                    min_path = path
                return path
                
            path += 1
            visited_maze[x][y] = 1
            print("v maze 1 : ", visited_maze)
            
            dfs((x, y, path), visited_maze)
            
            visited_maze[x][y] = 0
            print("v maze 2 : ", visited_maze)
            print("path 2 : " ,path)
            # if min_path > path:
            #     min_path = path
            #     print("@@@@")
            #     return min_path
    

# queue로 좌표를 저장해놓고 pop을 하면서 백트레킹을 적용해보면?

if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        print("#{} {}".format(i, solve()))