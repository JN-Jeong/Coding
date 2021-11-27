from collections import deque

T = int(input())

dx = [0,0,1,-1] # 좌우
dy = [1,-1,0,0] # 상하

def bfs(a, b, loc):
    q = deque()
    q.append((a,b))
    loc[a][b] = 0

    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N: # 땅의 범위를 벗어났을 때 continue
                continue
            if loc[nx][ny] == 1: # 값이 1이라면(배추가 심어져있다면)
                loc[nx][ny] = 0
                q.append((nx, ny))
    return

for _ in range(T):
    M, N, K = (map(int, input().split()))
    loc = [[0]*N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        loc[x][y] = 1
    
    worm = 0

    for i in range(M):
        for j in range(N):
            if loc[i][j] == 1:
                bfs(i, j, loc)
                worm += 1

    print(worm)