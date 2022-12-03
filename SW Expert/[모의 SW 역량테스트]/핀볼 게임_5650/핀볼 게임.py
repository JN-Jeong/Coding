"""
게임에서 얻을 수 있는 최대 점수 구하기
- 게임판 위에서 출발 위치와 진행 방향을 임의로 정할 수 있음
- 빈 공간 위치만 출발 가능

핀볼 : 상, 하, 좌, 우 중 한 방향으로 움직임
웜홀 : 입구와 출구가 존재, 입구로 들어가면 출구 위치로 나옴, 진행 방향은 그대로 유지
블랙홀 : 블랙홀에 빠지면 게임 종료
수평면 또는 수직면 : 진행 방향을 반대로 바꿈
경사면 : 진행 방향을 직각으로 바꿈

종료 조건
- 핀볼이 출발 위치로 돌아올 때
- 핀볼이 블랙홀에 빠질 때
- 종료되면 획득한 점수 반환

점수 획득 조건
- 벽에 부딪히면 +1
- 블록에 부딪히면 +1
- 웜홀을 통과하는 것은 점수 없음

구현 해야 할 함수
- 웜홀
- 블랙홀
- 수평면과 경사면
- 벽

입력
- 게임판 크기 (5 <= N <= 100, N x N)
- 게임판 (웜홀 : 6~10, 블랙홀 : -1, 빈공간 : 0, 블록 : 1~5)


웜홀
- 입력 : 입구 위치, 웜홀 번호
- 출력 : 출구 위치
- 입구 위치를 입력으로 주면 출구 위치를 알 수 있어야함 <- dictionary

블랙홀
- 입력 : 위치
- 게임 종료

수평면과 경사면
- 입력 : 위치, 진행 방향, 블록 번호
- 출력 : 진행 방향
- 점수 +1

벽
- 입력 : 위치
- 출력 : 진행 방향
- 점수 +1


실수했던 부분
- 상하좌우 방향을 잘못 설정함 (상 : row -1, 하 : row +1, 좌 : col -1, 우 : col +1, 기억하기)
- 웜홀 함수에서 출구 위치가 아니라 입구 위치를 반환하도록 했음.. (커뮤니티에서 보고 찾아냄..)


"""


d = ((-1,0), (1,0), (0,-1), (0,1)) # 4 방향
    #  상      하      좌      우
    #  0       1       2       3  

def wormhole(row, col, num):    # row, col : 위치, num : 웜홀 번호
    out_row1, out_col1 = wormholes[num][0]
    out_row2, out_col2 = wormholes[num][1]

    if out_row1 == row and out_col1 == col:
        return out_row2, out_col2
    elif out_row2 == row and out_col2 == col:
        return out_row1, out_col1

# def blackhole(i, j):    # 게임 종료
#     pass

def block(dir, num):  # dir : 방향, num : 블록 번호
    if num == 1:
        if dir == 2:    # 진행 방향이 왼쪽
            dir = 0
        elif dir == 1:  # 진행 방향이 아래쪽
            dir = 3
        else:
            dir = dirReverse(dir)
    elif num == 2:
        if dir == 2:    # 진행 방향이 왼쪽
            dir = 1
        elif dir == 0:  # 진행 방향이 위쪽
            dir = 3
        else:
            dir = dirReverse(dir)
    elif num == 3:
        if dir == 3:    # 진행 방향이 오른쪽
            dir = 1
        elif dir == 0:  # 진행 방향이 위쪽
            dir = 2
        else:
            dir = dirReverse(dir)
    elif num == 4:
        if dir == 3:    # 진행 방향이 오른쪽
            dir = 0
        elif dir == 1:  # 진행 방향이 아래쪽
            dir = 2
        else:
            dir = dirReverse(dir)
    elif num == 5:
        dir = dirReverse(dir)

    return dir


def wall(i, j):     # 벽 체크, i, j : 위치
    if i < 0 or j < 0 or i >= N or j >= N:
        return True
    else:
        return False

def dirReverse(dir):    # 방향 반대로 전환
    if dir == 0:
        dir = 1
    elif dir == 1:
        dir = 0
    elif dir == 2:
        dir = 3
    elif dir == 3:
        dir = 2

    return dir


def p(i, j):
    temp = []
    for row in range(N):
        if i == row:
            for col in range(N):
                if j == col:
                    temp += [0]
                else:
                    temp += [board[row][col]]
            print(temp)
        else:
            print(board[row])


T = int(input())

for i in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    starts = []     # 출발 위치 리스트
    wormholes = {}  # 웜홀 위치 딕셔너리
    for row in range(N):
        for col in range(N):
            if board[row][col] == 0:
                starts.append((row, col))   # 출발 위치 저장

            if 6 <= board[row][col] <= 10:  # 웜홀 위치 저장
                if board[row][col] not in wormholes:
                    wormholes[board[row][col]] = []
                wormholes[board[row][col]].append((row, col))
    # print(len(starts))
    # print(wormholes)
    maxScore = 0

    for start in starts:    # 핀볼 출발 위치
        for dir in range(4):    # 4 방향
            row = start[0] + d[dir][0]
            col = start[1] + d[dir][1]
            score = 0

            while True:
                if maxScore < score:                        # 최대 점수 갱신
                    maxScore = score
                if row == start[0] and col == start[1]:     # 핀볼이 출발 위치로 돌아오면 게임 종료
                    break

                if wall(row, col):                                                  # 벽이라면 방향 반대로 전환, 점수 +1
                    dir = dirReverse(dir)
                    score += 1
                elif board[row][col] == -1:                                         # 블랙홀 만남, 종료
                    break
                elif 1 <= board[row][col] <= 5:                                     # 블록 만남, 방향 바뀜, 점수 +1
                    dir = block(dir, board[row][col])
                    score += 1
                elif 6 <= board[row][col] <= 10:                                    # 웜홀 만남, 위치 바뀜
                    # print(row, col)
                    row, col = wormhole(row, col, board[row][col])
                    # print(row, col)
                
                # 핀볼 움직임 확인
                # print(score)
                # p(row, col)
                
                row += d[dir][0]
                col += d[dir][1]
                
            # print(start, score)
    
    print(f"#{i} {maxScore}")