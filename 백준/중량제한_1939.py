"""
C가 최대 10억이기 때문에 일반적인 방법으로 풀 수 없음
log or root가 적용되어야 함
"""

# # 메모리 초과
# N, M = map(int, input().split())
# islands = [[0]*(N+1) for _ in range(M+1)]

# for _ in range(M):
#     x, y, weight = map(int, input().split())
#     islands[x][y] = islands[y][x] = weight

# factory = list(map(int, input().split()))


# q = []
# q.append(factory[0])
# visited = [0] * (N+1)
# max_weight = 1000000000

# while q:
#     island = q.pop(0)
#     visited[island] = 1
    
#     for i in range(N+1):
#         if visited[i] == 0 and islands[island][i] != 0:
#             if i == factory[1]:
#                 visited[i] = 1
#                 if max_weight > islands[island][i]:
#                     max_weight = islands[island][i]
#             else:
#                 visited[i] = 1
#                 q.append(i)

# print(max_weight)



# 패캠 강의 풀이
def bfs(c):
    q = []
    q.append(factory[0])
    visited = [0] * (N+1)
    visited[factory[0]] = 1

    while q:
        island = q.pop(0)

        for i, weight in islands[island]:
            if visited[i] == 0 and weight >= c:
                if i == factory[1]:
                    return True
                else:
                    visited[i] = 1
                    q.append(i)
    
    return False


N, M = map(int, input().split())
islands = [[]*(N+1) for _ in range(N+1)]

start = 1
end = 1000000000

for _ in range(M):
    x, y, weight = map(int, input().split())
    islands[x].append((y, weight))
    islands[y].append((x, weight))

factory = list(map(int, input().split()))

result = start
while start <= end:
    mid = (start + end) // 2        # mid는 현재의 중량을 의미
    if bfs(mid):                    # 이동이 가능하므로 중량 증가
        result = mid
        start = mid + 1
    else:                           # 이동이 불가능하므로, 중량 감소
        end = mid - 1

print(result)