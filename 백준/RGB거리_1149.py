# '''
# 시간초과
# '''

# N = int(input())
# costs = [list(map(int, input().split())) for _ in range(N)]

# res = 1e10

# def solve(depth, color, cost):
#     global res
#     if depth == N:
#         # print(res, cost)
#         res = min(res, cost)
#         return

#     for i in range(3):
#         if i == color:
#             continue
#         solve(depth+1, i, cost + costs[depth][i])

# solve(0, 0, 0)  # R 색칠
# solve(0, 1, 0)  # G 색칠
# solve(0, 2, 0)  # B 색칠
# print(res)




N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

res = 1e10

for i in range(1, N):
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]   # R 색칠
    costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]   # G 색칠
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + costs[i][2]   # B 색칠

print(min(costs[N-1]))