N, M = map(int, input().split())
board = [input() for _ in range(N)]
# print(board)

WB = ['W', 'B']
BW = ['B', 'W']

rows = [[WB[i % 2] for i in range(8)], [BW[i % 2] for i in range(8)]]

WB_board = [rows[i % 2] for i in range(8)]
BW_board = [rows[i % 2] for i in range(1, 8+1)]

# for wb in WB_board:
#     print(wb)
# print()
# for bw in BW_board:
#     print(bw)

min_ = 123456789
for i in range(len(board)-8 + 1):
    for j in range(len(board[0])-8 + 1):
        wb, bw = 0, 0
        for row in range(8):
            for col in range(8):
                if board[i+row][j+col] != WB_board[row][col]:
                    wb += 1
                if board[i+row][j+col] != BW_board[row][col]:
                    bw += 1
        min_ = min(min_, wb, bw)

print(min_)