"""
종료 조건
- 모든 코어를 방문하면 종료
- 방문한 코어의 개수가 같고 연결된 전선 길이가 더 길면 종료 (백트래킹)



"""

delta = ((1,0), (0,-1), (-1,0), (0,1)) # 상하좌우

def delete(row, col, dir, line): # 전선 삭제 / 행, 열, 상하좌우, 전선 수
    dr, dc = delta[dir] # dir = 0~3 (상하좌우)
    
    for _ in range(line): # 전선 수 만큼 반복
        proc_map[row+dr][col+dc] = 0
        row += dr
        col += dc

def connect(row, col, dir): # 연결된 전선 개수 반환
    srow = row
    scol = col
    dr, dc = delta[dir]
    lines = 0
    while 0 <= row + dr < N and 0 <= col + dc < N: # 프로세서 범위 내에서 반복
        row += dr
        col += dc
        if proc_map[row][col]: # 연결할 전선 위치에 core 또는 전선이 존재한다면 종료
            break
        proc_map[row][col] = 1 # 전선 연결
        lines += 1 # 전선 개수 +1
    else: # if가 실행되지 않고 while이 종료된다면 전선 수 반환
        return lines
    delete(srow, scol, dir, lines) # if가 실행된다면 추가했던 전선을 삭제하고 0을 반환
    return 0

def DFS(now, last, line):
    global maxCores, minLine
    if maxCores < len(now):
        maxCores = len(now)
        minLine = 12*12+1
    if maxCores == len(now) and minLine > line:
        minLine = line

    for i in range(last, len(cores)):
        for dir in range(4):
            lines = connect(*cores[i], dir)
            if not lines:
                continue
            next = now[:]
            next.append(i)
            print(next)
            # print("last, dir : ", last, dir)
            # print()
            DFS(next, i + 1, line + lines)
            delete(*cores[i], dir, lines)

T = int(input())

for t in range(1, T+1):
    N = int(input())
    proc_map = [list(map(int, input().split())) for _ in range(N)] # 프로세서 map

    cores = [] # core의 index 저장
    for i in range(1, N-1):
        for j in range(1, N-1):
            if proc_map[i][j] == 1:  # 해당 위치에 Core가 존재한다면
                if not(i == 0 or i == N - 1 or j == 0 or j == N - 1):
                    cores.append((i,j))

    maxCores = -1
    minLine = 12*12+1
    DFS([], 0, 0)
    print("#{} {}".format(t, minLine))