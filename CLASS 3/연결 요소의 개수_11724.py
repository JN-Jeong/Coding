"""
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1
6 5
1 2
2 5
5 1
3 4
4 6

예제 출력 1
2

예제 입력 2
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

예제 출력 2
1
"""

import sys

sys.setrecursionlimit(100000)  # dfs 사용 시 재귀의 깊이를 더 늘려줘야 한다.(아니면 런타임 오류 발생)

N, M = map(int, sys.stdin.readline().split())  # input은 시간초과

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())  # input은 시간초과
    graph[u][v] = graph[v][u] = 1

print(graph)
visited = [0] * (N + 1)
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
