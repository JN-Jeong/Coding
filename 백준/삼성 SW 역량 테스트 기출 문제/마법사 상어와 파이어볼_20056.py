"""
1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다
"""


def solution():
    answer = 0
    N, M, K = map(int, input().split())  # 보드 크기, 파이어볼 개수, 반복 횟수
    board = [[[] for _ in range(N)] for _ in range(N)]

    for row in range(M):
        row, col, m, speed, direction = map(int, input().split())
        board[row - 1][col - 1].append((m, speed, direction))  # 질량, 스피드, 방향
    for b in board:
        print(b)
    print()

    dir = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

    for _ in range(K):
        temp_board = [[[] for _ in range(N)] for _ in range(N)]

        # 1. 이동하기
        for row in range(N):
            for col in range(N):
                while board[row][col]:
                    m, s, d = board[row][col].pop()
                    n_row = (row + dir[d][0] * s) % N
                    n_col = (col + dir[d][1] * s) % N

                    temp_board[n_row][n_col].append((m, s, d))  # 질량, 스피드, 방향

        board = temp_board.copy()

        print("# 1. 이동 후")
        for b in board:
            print(b)
        print()

        temp_board = [[[] for _ in range(N)] for _ in range(N)]

        for row in range(N):
            for col in range(N):
                m, s, n = 0, 0, 0  # 질량, 스피드, 합쳐진 파이어볼 개수
                even_d, odd_d = 0, 0  # 짝수 합, 홀수 합

                # 2. 2개 이상의 파이어볼이 있는 칸
                if len(board[row][col]) >= 2:
                    # 2-1. 같은 칸의 파이어볼 합치기
                    while board[row][col]:
                        # m, d, s += board[row][col].pop()
                        temp = board[row][col].pop()
                        m += temp[0]
                        s += temp[1]
                        if temp[2] % 2 == 0:  # 방향이 짝수라면
                            even_d += 1
                        else:  # 방향이 홀수라면
                            odd_d += 1
                        n += 1

                    board[row][col].append((m, s, 0))
                    print("## 2-1. 파이어볼 합치기")
                    for b in board:
                        print(b)
                    print()

                    # 2-2, 3. 4개의 파이어볼로 나누기
                    new_m = m // 5
                    if new_m < 1:  # 질량이 0인 파이어볼은 소멸
                        continue

                    new_s = s // n
                    if even_d == n or odd_d == n:  # 방향이 모두 짝수이거나 홀수일 때 방향 : 0, 2, 4, 6
                        for i in range(0, len(dir), 2):
                            # 질량, 스피드, 방향
                            temp_board[row][col].append((new_m, new_s, i))

                    else:  # 방향 : 1, 3, 5, 7
                        for i in range(1, len(dir), 2):
                            # 질량, 스피드, 방향
                            temp_board[row][col].append((new_m, new_s, i))

                elif len(board[row][col]) >= 1:
                    temp_board[row][col].append(board[row][col].pop())

        board = temp_board.copy()
        print("### 1, 2 후 결과")
        for b in board:
            print(b)
        print()

    for i in range(N):
        for j in range(N):
            for m, _, _ in board[i][j]:
                answer += m

    return answer


if __name__ == "__main__":
    print(solution())
