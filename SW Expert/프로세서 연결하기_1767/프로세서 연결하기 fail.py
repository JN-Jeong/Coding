# delta = ((1,0), (0,-1), (0,-1), (0,1)) # 상하좌우 (이렇게 하면 틀림)
delta = ((0,1), (1,0), (-1,0), (0,-1)) # 하우좌상

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
    while 0 <= row + dr < N and 0 <= col + dc < N: # 프로세서 map 범위 내에서 반복
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

def DFS(now, last, line): # list, int, int / now : 방문한 core 위치 리스트, last : 마지막 방문한 core 위치, line : 현재 연결된 line 길이
    global maxCores, minLine
    if maxCores < len(now):
        maxCores = len(now)
        minLine = 12*12+1
    if maxCores == len(now) and minLine > line:     # 모든 core를 방문했거나 최소 전선 길이보다 짧다면 전선 길이 갱신
        minLine = line

    for i in range(last, len(cores)):   # 모든 core 방문하면 종료
        for dir in range(4):
            lines = connect(*cores[i], dir)     # 상하좌우 방향에서 현재 방향으로 연결한 선 길이 반환, 연결된 선이 없다면 continue
            if not lines:
                continue
            next = now[:]   # [:]는 now와 다른 주소값이 할당됨, next를 바꾸더라도 now에 영향을 끼치지 않음, 방문한 core 위치 리스트 복사해주고
            next.append(i)  # 현재 위치도 추가해줌
            print("now : ", next)
            # print("last : ", i+1)
            # print("line : ", line+lines)
            DFS(next, i + 1, line + lines)      # 갱신된 방문 core 위치 리스트, 마지막 방문한 core 위치 갱신, 현재 연결된 line 길이 갱신)
            delete(*cores[i], dir, lines)       # 다음 방향에 영향을 끼치지 않기 위해 방금 연결한 선 해제
                                                # *cores[i] : 마지막에 연결한 core 위치(*cores[i] 로 인자를 넘겨주면 cores[i][0] cores[i][1]이 전달됨), dir : 연결한 선 방향, lines : 연결한 선 개수

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

    print(cores)

    maxCores = -1
    minLine = 12*12+1
    DFS([], 0, 0)
    print("#{} {}".format(t, minLine))