"""
가장 처음에 양분은 모든 칸에 5만큼 들어있다.

사계절이 있음
봄
1. 나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가
2. 각각의 나무는 나무가 있는 1x1 크기의 칸에 있는 양분만 먹을 수 있음
3. 한 칸에 여러 나무가 있다면 나이가 어린 나무부터 양분을 먹음
4. 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 즉시 죽음

여름
1. 봄에 죽은 나무가 양분으로 변함
2. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가됨, 소수점 아래는 버림

가을
1. 나무가 번식함, 번식하는 나무는 나이가 5의 배수여야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생김 
(어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1))
2. 상도의 땅을 벗어나는 칸에는 나무가 생기지 않음

겨울
1. 로봇이 돌아다니면서 땅에 양분을 추가한다.
2. 각 칸에 추가되는 양분의 양은 A[r][c]이다.

K년이 지난 후 살아있는 나무의 개수?

N : 땅 크기
M : 구입한 나무 개수
K : 종료 조건
"""


def solution():
    N, M, K = map(int, input().split())

    board = [[5] * N for _ in range(N)]  # 양분을 저장한 땅 (가장 처음에 양분은 모든 칸에 5만큼 들어있다)
    for b in board:
        print(b)

    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    trees = []
    for _ in range(M):
        trees.append(list(map(int, input().split())))
    trees.sort(key=lambda x: x[2])

    # print(A)
    # print(trees)

    for i in range(K):
        board, trees, lives = spring(board, trees)
        board, trees = summer(board, trees, lives)
        trees = autumn(board, trees)
        board = winter(board, A)

    print(trees)
    return len(trees)


def spring(board, trees):
    lives = [1] * len(trees)
    for i in range(len(trees)):
        row, col, age = trees[i]
        row, col = row - 1, col - 1
        board[row][col] -= age

        if board[row][col] < 0:  # 양분을 먹을 수 없음
            lives[i] = 0  # 나무 죽음
            board[row][col] += age  # 양분 다시 되돌림

        else:
            trees[i][2] += 1  # 나무 나이 먹음

    return board, trees, lives


def summer(board, trees, lives):
    for b in board:
        print(b)
    for i in range(len(lives)):
        row, col, age = trees[i]
        row, col = row - 1, col - 1
        if lives[i] == 0:  # 죽은 나무
            board[row][col] += age // 2  # 양분 추가
            trees[i][2] = 0  # 나이 0으로 만듬
    print(trees)
    for b in board:
        print(b)
    print("-" * 20)

    i = 0
    while i < len(trees):  # 나무 리스트 갱신 (죽은 나무 제거)
        if trees[i][2] == 0:
            trees.pop(i)
            i -= 1
        i += 1

    return board, trees


def is_not_wall(board, row, col):  # 땅을 벗어나지 않았다면 True, 벗어나면 False 반환
    if (0 <= row < len(board)) and (0 <= col < len(board[0])):
        return True
    return False


# (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1))
def autumn(board, trees):
    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    n = len(trees)
    for i in range(n):
        row, col, age = trees[i]
        row, col = row - 1, col - 1
        if age % 5 == 0:  # 번식 대상
            for dr, dc in dir:
                nr, nc = row + dr, col + dc
                if is_not_wall(board, nr, nc):
                    trees.append([nr, nc, 1])  # 나무 추가

    trees.sort(key=lambda x: x[2])
    return trees


def winter(board, A):
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += A[i][j]  # 땅에 양분 추가

    return board


if __name__ == "__main__":
    print(solution())
