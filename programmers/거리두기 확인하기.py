"""
2021 카카오 채용연계형 인턴십
거리두기 확인하기
"""
from collections import deque


def solution(places):
    answer = []

    # 상좌하우
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    def isin(y, x):
        if 0 <= y < 5 and 0 <= x < 5:
            return True
        return False

    def bfs(i, j, place, visited):
        q = deque()
        q.append([i, j, 0])
        visited[i][j] = 1

        while q:
            y, x, cnt = q.popleft()

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if isin(ny, nx) and visited[ny][nx] == 0:
                    if place[ny][nx] == "O":
                        visited[ny][nx] = cnt + 1
                        q.append([ny, nx, cnt + 1])
                    elif place[ny][nx] == "P":
                        visited[ny][nx] = cnt + 1
                        q.append([ny, nx, 0])
                        if cnt <= 1:
                            return False

            # for v in visited:
            #     print(v)
            # print()

        return True

    def check(place, visited):
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    result = bfs(i, j, place, visited)
                    if not result:
                        return False

        return True

    for place in places:
        visited = [[0] * 5 for _ in range(5)]
        flag = check(place, visited)
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer


if __name__ == "__main__":
    places = [
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    ]
    results = [[1, 0, 1, 1, 1]]

    for i, data in enumerate(places):
        p = data
        print(f"#{i}", solution(p))
