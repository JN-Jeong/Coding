"""
종료 조건
- 모든 코어를 방문하면 종료

필요한 변수
- 코어 개수
- 프로세서 cell (map)
- 현재 선택한 코어 개수
- 현재 연결된 전선 길이

실수했던 부분들
- 전원을 연결할 수 없는 코어가 존재하는 경우도 있음 (모든 코어가 전원을 연결할 수 없는 경우에는 전선 길이가 0)
- 더 많은 코어를 연결할 수 있으면 바로 갱신해줘야 함 (중요) -> 더 많은 코어를 연결하는 것이 1순위, 그 이후에 전선 길이가 최소가 되어야 함 (이거 때문에 시간 많이 잡아먹음)

출력 (최대한 많은 코어에 전원을 연결했을 때, 최대한 많은 코어를 연결)
- 연결된 전선 길이 (최소)

"""

d = ((0,1), (0,-1), (-1,0), (1,0)) # 4 방향

def solve(idx, numCore, lenLine):  # 방문 코어 index,  연결한 코어 개수, 연결된 전선 길이, 프로세서 cell
    global minLine
    global maxCore
    # print(idx, numCore, lenLine)
    if idx == len(cores): # 모든 코어를 방문하면 최소 전선 길이 갱신
        if maxCore < numCore:  # 연결한 코어 수가 많으면 바로 연결한 코어 수와 최소 전선 길이 갱신
            maxCore = numCore
            minLine = lenLine
        
        if maxCore == numCore and minLine > lenLine:    # 연결한 코어 수는 같으나 전선 길이가 최소 전선 길이보다 전선 길이 작으면 갱신
            minLine = lenLine

    if idx >= len(cores):   # 방문할 코어가 없으면 종료
        return

    row, col = cores[idx]   # 방문한 코어의 위치
    for dir in range(4):
        line = connect(row, col, dir)  # 전선 연결
        if line:
            solve(idx + 1, numCore + 1, lenLine + line)    # 현재 코어에 전원 연결한 후 다음 코어 방문
            # print("conn : ", proc_map)
            disconnect(row, col, dir, line)    # 다음 방향으로 전선 연결할 때 영향을 주지 않기 위해 연결했던 전선 해제
            # print("disc : ", proc_map)
    solve(idx + 1, numCore, lenLine)   # 현재 코어에 전원 연결하지 않고 다음 코어 방문


# 전선 연결
def connect(row, col, direction):  # 코어의 위치(row, col), 전선 연결 방향, 프로세서 cell
    line = 0
    nrow = row
    ncol = col
    while True:
        nrow += d[direction][0]
        ncol += d[direction][1]
        if nrow < 0 or ncol < 0 or nrow >= N or ncol >= N:  # 전원을 연결하면(프로세서 cell 범위를 벗어나면) 연결한 전선 길이 반환
            return line
        if proc_map[nrow][ncol] == 1 or proc_map[nrow][ncol] == 2:    # 전원을 연결하기 전에 코어나 전선이 존재하면 연결한 전선 길이 반환
            disconnect(row, col, direction, line)   # 전원을 연결하지 않았으므로 전선 해제
            return False
        line += 1
        proc_map[nrow][ncol] = 2       # 프로세서 cell에 전선 연결 표시



# 전선 해제
def disconnect(row, col, direction, line):   # 코어의 위치(row, col), 전선 연결 방향, 연결한 전선 길이, 프로세서 cell
    for _ in range(line):
        row += d[direction][0]
        col += d[direction][1]
        proc_map[row][col] = 0


T = int(input())

for t in range(1, T+1):
    N = int(input())
    proc_map = [list(map(int, input().split())) for _ in range(N)]
    # print(proc_map)

    cores = []      # 코어의 위치 리스트
    for i in range(1, N-1):
        for j in range(1, N-1):
            if proc_map[i][j] == 1:
                cores.append((i, j))
    # print(cores)

    minLine = 12 * 12   # cell의 최대 크기가 12
    maxCore = -1
    
    solve(0, 0, 0)

    if maxCore < 0:     # 전원에 연결된 코어가 존재하지 않으면 0 출력
        print(f"#{t} {0}")
    else:
        print(f"#{t} {minLine}")