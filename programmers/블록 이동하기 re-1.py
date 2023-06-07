from collections import deque


def solution(board):
    answer = 0
    nboard = [[1] * (len(board) + 1 + 1) for _ in range(len(board) + 1 + 1)]  # 벽으로 맵 확장

    for i in range(len(board)):
        for j in range(len(board[0])):
            nboard[i + 1][j + 1] = board[i][j]

    # for b in nboard:
    #     print(b)

    q = deque()
    q.append(((1, 1), (1, 2), 0))  # 로봇의 위치 좌표, 이동 횟수
    confirm = set([((1, 1), (1, 2))])  # 이미 방문한 좌표 저장 (중복 방문 방지), ※ [((1,1), (1,2))]가 아니라 (((1,1), (1,2))) 처럼 튜플로 만들면 (1,1), (1,2) 각각 원소로 들어감

    N = len(board)
    while q:
        loc1, loc2, cnt = q.popleft()
        if loc1 == (N, N) or loc2 == (N, N):
            return cnt

        for movement in move([loc1, loc2], nboard):
            # print("@ next movement : ", movement)
            if movement not in confirm:
                q.append((movement[0], movement[1], cnt + 1))
                confirm.add(movement)

    return answer  # 항상 목적지에 도착할 수 있는 경우만 입력으로 주어지기 때문에 없어도 됨


def is_wall(loc, board):  # 벽이면 True를 반환
    st, nd = loc[0], loc[1]
    if board[st[0]][st[1]] == 1 or board[nd[0]][nd[1]] == 1:
        return True
    return False


# 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 함
def move(loc, board):  # loc : 위치, board : 맵, cnt : 이동횟수
    movements = []
    robot1, robot2 = loc[0], loc[1]
    dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    # 상하좌우 이동
    for dx, dy in dir:
        nloc1 = (robot1[0] + dx, robot1[1] + dy)
        nloc2 = (robot2[0] + dx, robot2[1] + dy)
        if is_wall([nloc1, nloc2], board):
            continue
        movements.append((nloc1, nloc2))

    # 회전 이동
    if robot1[0] == robot2[0]:  # 가로 모양일 때 (첫 번째 위치와 두 번째 위치의 row 값이 같을 때)
        for d in [-1, 1]:
            nloc1 = (robot1[0] + d, robot1[1])
            nloc2 = (robot2[0] + d, robot2[1])
            if is_wall([nloc1, nloc2], board):
                continue
            movements.append((robot1, nloc1))
            movements.append((robot2, nloc2))

    else:  # 세로 모양일 때
        for d in [-1, 1]:
            nloc1 = (robot1[0], robot1[1] + d)
            nloc2 = (robot2[0], robot2[1] + d)
            if is_wall([nloc1, nloc2], board):
                continue
            movements.append((nloc1, robot1))
            movements.append((nloc2, robot2))

    # print("# next movements : ", movements)

    return movements
