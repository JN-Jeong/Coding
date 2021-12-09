import sys
sys.setrecursionlimit(100000) # dfs 사용 시 재귀의 깊이를 더 늘려줘야 한다.(아니면 런타임 오류 발생)

N, M = map(int, sys.stdin.readline().split()) # input은 시간초과

graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split()) # input은 시간초과
    graph[u][v] = graph[v][u] = 1

print(graph)
visited = [0] * (N+1)
CC = 0

def dfs(v):
    visited[v] = 1
    for i in range(1, len(graph)):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

for i in range(1, len(graph)):
    if visited[i] == 0:
        dfs(i)
        CC += 1

print(CC)