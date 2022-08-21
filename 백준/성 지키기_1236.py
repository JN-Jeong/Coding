# 패캠 강의 풀의
N, M = map(int, input().split())

castle = []
for _ in range(N):
    castle.append(input())

row = [0] * N
col = [0] * M

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row[i] = 1
            col[j] = 1

row_count = 0
for i in range(N):
    if row[i] == 0:
        row_count += 1

col_count = 0
for i in range(M):
    if col[i] == 0:
        col_count += 1

print(max(row_count, col_count))    # 각각의 행과 열에 대해 경비원이 존재하지 않는 최대 값이 경비원이 필요한 최소 수가 됨