"""
4 7
6 13
4 8
3 6
5 12
14
----------
4 7
6 13
4 8
3 9
5 12

최대 무게가 1일 때 가질 수 있는 최대 가치 값과 
최대 무게가 2일 때 가질 수 있는 최대 가치 값을 
더하면 최대 무게가 3일 때 최대 가치가 될 수 있음
(무게가 3인 물건의 가치가 더 높을 수도 있음)
"""


# N, K = map(int, input().split())
# stuffs = [[0, 0]]
# for _ in range(N):
#     stuffs.append(list(map(int, input().split())))

# memo = [[0] * (K + 1) for _ in range(N + 1)]
# for i in range(1, N + 1):  # 물건들 기준
#     for j in range(1, K + 1): # 무게 기준
#         weight, value = stuffs[i][0], stuffs[i][1]

#         if j < weight:
#             memo[i][j] = memo[i - 1][j]
#         else:
#             memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - weight] + value)

# print(memo[N][K])


N, K = map(int, input().split())

memo = [0] * (K + 1)    # 담은 무게 저장
print(memo)
for i in range(N):
    weight, value = map(int, input().split())
    for j in range(K, weight - 1, -1):
        memo[j] = max(memo[j], memo[j - weight] + value)    # (현재 무게에 담긴 가치)와 (현재 가치 + 한도까지 남은 무게의 최대 가치) 중 최댓값으로 갱신
    print(memo)
print(memo[-1])