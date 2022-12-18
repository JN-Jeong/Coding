from collections import deque


N = int(input())

maps = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
complexes = []

def BFS(x, y):
    q = deque()
    q.append((x, y))

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    apart = 0

    while q:
        loc_x, loc_y = q.popleft()

        if visited[loc_x][loc_y] == 0 and maps[loc_x][loc_y] == '1': # 방문하지 않은 곳에 아파트 발견
            visited[loc_x][loc_y] = 1
            apart += 1
            print(visited)

            for i in range(4):
                nx = loc_x + dx[i]
                ny = loc_y + dy[i]

                if 0 <= nx < N and 0 <= ny < N:
                    q.append((nx, ny))

    if apart > 0:
        complexes.append(apart)

for i in range(N):
    for j in range(N):
        BFS(i, j)

complexes.sort() # 단지내 집의 수 오름차순으로 정렬
print(len(complexes))
for i in range(len(complexes)):
    print(complexes[i])