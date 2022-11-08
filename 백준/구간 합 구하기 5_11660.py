# # 시간초과
# N, M = map(int, input().split())
# tables = [[0] * (N+1)]
# for _ in range(N):
#     tables.append([0] + list(map(int, input().split())))

# for t in tables:
#     print(t)

# sum_tables = tables.copy()
# # sum_tables[1][1] = tables[0][0]

# for i in range(1, N+1):
#     for j in range(1, N):
#         sum_tables[i][j + 1] += sum_tables[i][j]

# for j in range(1, N+1):
#     for i in range(1, N):
#         sum_tables[i + 1][j] += sum_tables[i][j]


# for t in sum_tables:
#     print(t)


# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     print(sum_tables[x2][y2] - (sum_tables[x1 - 1][y2] + sum_tables[x2][y1 - 1]) + sum_tables[x1 - 1][y1 - 1])


# sys.stdin.readline()으로 통과
import sys

N, M = map(int, sys.stdin.readline().split())
tables = [[0] * (N+1)]
for _ in range(N):
    tables.append([0] + list(map(int, sys.stdin.readline().split())))

for t in tables:
    print(t)

sum_tables = tables.copy()
# sum_tables[1][1] = tables[0][0]

for i in range(1, N+1):
    for j in range(1, N):
        sum_tables[i][j + 1] += sum_tables[i][j]

for j in range(1, N+1):
    for i in range(1, N):
        sum_tables[i + 1][j] += sum_tables[i][j]


for t in sum_tables:
    print(t)


for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sum_tables[x2][y2] - (sum_tables[x1 - 1][y2] + sum_tables[x2][y1 - 1]) + sum_tables[x1 - 1][y1 - 1])
