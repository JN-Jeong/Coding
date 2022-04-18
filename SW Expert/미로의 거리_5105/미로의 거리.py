"""
3,3 , 2,3 , 1,3 , 0,3 까지 갔다가 도착 지점을 찾지 못하면 <= 이쪽에는 도착 지점이 없다는 것을 어떻게 확인?
왔던 경로를 다시 되돌아가고 (visited_maze, 왔던 경로는 벽으로 설정)
다음 경로를 탐색
도착 지점을 찾을 때 까지 반복
- 잘못된 접근 -
"""

"""
좌표뿐만 아니라 별도의 경로 칸 수를 deque에 함께 저장
모든 경로 방문
도착 지점에 도달하면 해당 경로 칸 수(-1, 최소 경로)를 반환
- 정답 -
"""

from queue import PriorityQueue


def solve():
    N = int(input())

    global maze
    maze = [list(input()) for _ in range(N)]

    print(maze)

    start = PriorityQueue()
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "2":
                # start = [(i, j, 0)] # 시작 좌표와 0을 가지도록 함
                start.put((0, i, j)) # 우선순위 큐를 활용하여 최소 거리 보장

    print(start)
    return bfs(start)


def is_path(loc): # 통로이면 True 반환, 아니면 False 반환
    global maze
    x, y = loc
    if x < 0 or y < 0 or x >= len(maze[0]) or y >= len(maze) or maze[x][y] == "1":
        return False
    else:
        return True


def bfs(loc):
    global maze
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited_maze = [[0] * len(maze) for _ in range(len(maze[0]))]

    while not loc.empty():
        # start_x, start_y, now_path = loc.pop()
        now_path, start_x, start_y = loc.get()
        visited_maze[start_x][start_y] = 1

        if maze[start_x][start_y] == "3": # 도착했다면 경로 칸 수 반환
            print("3 : ", now_path)
            return now_path - 1

        for i in range(4): # 상하좌우
            x = start_x + dx[i]
            y = start_y + dy[i]

            if is_path((x,y)) and visited_maze[x][y] == 0:
                # loc.append((x,y,now_path+1))
                loc.put((now_path+1, x, y))
                visited_maze[x][y] = 1

            print("loc : ", loc)
        print(visited_maze)
    return 0


if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        print("#{} {}".format(i, solve()))