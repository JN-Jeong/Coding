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


from collections import deque


def solution():
    answer = 0
    N, M, K = map(int, input().split())

    board = [[5] * N for _ in range(N)]  # 양분을 저장한 땅 (가장 처음에 양분은 모든 칸에 5만큼 들어있다)
    for b in board:
        print(b)

    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    trees = [[deque() for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, z = map(int, input().split())
        trees[x - 1][y - 1].append(z)

    for t in trees:
        print(t)

    for _ in range(K):
        board, trees = spring_summer(board, trees)
        for b in board:
            print(b)
        trees = autumn(board, trees)
        for t in trees:
            print(t)
        board = winter(board, A)

    for tree in trees:
        for t in tree:
            answer += len(t)

    return answer


def spring_summer(board, trees):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if trees[i][j]:
                for k in range(len(trees[i][j])):
                    age = trees[i][j][k]
                    if age <= board[i][j]:  # spring
                        board[i][j] -= age
                        trees[i][j][k] += 1
                    else:  # summer
                        for _ in range(k, len(trees[i][j])):
                            board[i][j] += trees[i][j].pop() // 2
                        break

    return board, trees


def is_not_wall(board, row, col):  # 땅을 벗어나지 않았다면 True, 벗어나면 False 반환
    if (0 <= row < len(board)) and (0 <= col < len(board[0])):
        return True
    return False


# (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1))
def autumn(board, trees):
    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if trees[i][j]:
                for k in range(len(trees[i][j])):
                    if trees[i][j][k] % 5 == 0:  # 나무의 나이가 5의 배수일 때 번식
                        for dx, dy in dir:
                            nx, ny = i + dx, j + dy
                            if is_not_wall(board, nx, ny):
                                trees[nx][ny].appendleft(1)

    return trees


def winter(board, A):
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += A[i][j]  # 땅에 양분 추가

    return board


if __name__ == "__main__":
    print(solution())
