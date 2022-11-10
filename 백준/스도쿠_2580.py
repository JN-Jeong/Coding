sudoku = [list(map(int, input().split())) for _ in range(9)]
print(sudoku)

loc = []
for i in range(len(sudoku)):
    for j in range(len(sudoku)):
        if sudoku[i][j] == 0:
            loc.append((i, j))
print(loc)

# 0~2 : 3으로 나누면 0
# 3~5 : 3으로 나누면 1
# 6~8 : 3으로 나누면 2

def check(row, col, num):
    # 행 체크
    for i in range(len(sudoku)):
        if sudoku[row][i] == num:       # num이랑 같은지 확인?? -> 해당 행에 같은 숫자가 존재하는지 확인
            return False

    # 열 체크
    for i in range(len(sudoku[0])):
        if sudoku[i][col] == num:       # num이랑 같은지 확인?? -> 해당 열에 같은 숫자가 존재하는지 확인
            return False

    # 정사각형 체크
    for i in range(3):
        for j in range(3):
            if sudoku[i + (row // 3) * 3][j + (col // 3) * 3] == num:       # num이랑 같은지 확인?? -> 해당 정사각형에 같은 숫자가 존재하는지 확인
                return False
    return True


def solve(idx):
    if idx == len(loc):
        for i in range(len(sudoku)):
            print(*sudoku[i])
        exit(0)
    
    for i in range(1, 10):    # i : 숫자
        r, c = loc[idx]
        print(r, c)
        if check(r, c, i):
            sudoku[r][c] = i
            solve(idx + 1)
            sudoku[r][c] = 0
        
solve(0)