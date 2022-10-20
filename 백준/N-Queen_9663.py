# pypy3로 제출

N = int(input())

def dfs(depth):
    global cnt
    # print("N : ", N)
    if depth == N:
        cnt += 1
        return

    for i in range(N):
        if visited[i] == 0:
            board[depth] = i

            if check(depth):
                # print(board, depth)
                visited[i] = 1      # 백트래킹
                dfs(depth + 1)
                visited[i] = 0      # 백트래킹

def check(x):      # 같은 행, 열 또는 대각선 위치에 있다면 False 반환, 아니라면 True 반환
    for i in range(x):
        if (board[x] == board[i]) or (abs(board[x] - board[i]) == (x - i)):     # (행끼리의 차 == 열끼리 차의 절댓값)이면 대각선 상에 위치한 것
            return False
    return True

cnt = 0
visited = [0] * N
board = [0] * N

dfs(0)
print(cnt)