"""
https://softeer.ai/practice/6248
[HSAT 6회 정기 코딩 인증평가 기출] 출퇴근길
"""

import sys

sys.setrecursionlimit(10**6)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
graphR = [[] for _ in range(n + 1)]  # reversed
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graphR[y].append(x)
print("@", graph)
print("@@", graphR)

S, T = map(int, input().split())


def dfs(now, graph, visited):
    if visited[now] == 1:
        return

    visited[now] = 1
    for node in graph[now]:
        dfs(node, graph, visited)


# 출근길
fromS = [0] * (n + 1)
fromS[T] = 1
dfs(S, graph, fromS)

# 퇴근길
fromT = [0] * (n + 1)
fromT[S] = 1
dfs(T, graph, fromT)

toS = [0] * (n + 1)
dfs(S, graphR, toS)

toT = [0] * (n + 1)
dfs(T, graphR, toT)

answer = 0
for i in range(1, n + 1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        answer += 1

print(answer - 2)
