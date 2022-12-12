def solution():
    answer = 0
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N**2)]

    board = [[0] * N for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for student in students:
        temp = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    like = 0
                    blank = 0
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if board[nx][ny] in student[1:]:
                                like += 1
                            if board[nx][ny] == 0:
                                blank += 1
                    temp.append([like, blank, i, j])
        """좋아하는 학생 수가 많을수록, 비어있는 칸이 많을수록, 행의 번호가 작을수록, 열의 번호가 작을수록 우선"""
        temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
        board[temp[0][2]][temp[0][3]] = student[0]

    students.sort()  # index로 접근할 수 있도록 정렬
    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] in students[board[i][j] - 1]:
                        total += 1
            if total != 0:
                answer += 10 ** (total - 1)

    return answer


if __name__ == "__main__":
    print(solution())
