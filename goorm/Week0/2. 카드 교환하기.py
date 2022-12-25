# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

N, M = map(int, input().split())
C = [0] + list(map(int, input().split()))
# print(C)

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

# print(graph)

q = deque()
visited = [0] * (N + 1)

components = []
for i in range(1, N + 1):
    if visited[i] == 0:
        q.append(i)
        visited[i] = 1
        temp = [i]
    else:
        temp = []
    while q:
        u = q.popleft()
        for v in range(1, N + 1):
            if graph[u][v] == 1 and visited[v] == 0:
                visited[v] = 1
                q.append(v)
                temp.append(v)

    if temp:
        components.append(temp)

answer = 0
for component in components:
    temp = []
    for num in component:
        temp.append(C[num])
    temp.sort()
    print(temp)
    for c, t in zip(component, temp):
        answer += abs(c - t)

print(components)
print(answer)
