from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]  # 주어지는 간선은 양방향

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1  # 그래프가 양방향이고 두 정점이 연결되었다면 1로 표시해줌

visited_dfs = [0] * (N + 1)


def dfs(v):
    visited_dfs[v] = 1  # 방문한 인덱스는 1로 표시해줌
    print(v, end=" ")  # 방문한 인덱스 출력
    for i in range(len(graph)):
        if (
            visited_dfs[i] == 0 and graph[v][i] == 1
        ):  # 방문하지 않은 인덱스이고 두 정점이 연결되어 있다면 재귀호출
            dfs(i)


visited_bfs = [0] * (N + 1)


def bfs(v):
    print()
    q = deque()
    q.append(v)
    visited_bfs[v] = 1  # 방문한 인덱스는 1로 표시해줌
    while q:  # q가 empty될 때까지
        v = q.popleft()
        print(v, end=" ")  # 방문한 인덱스 출력
        for i in range(len(graph)):
            if (
                visited_bfs[i] == 0 and graph[v][i] == 1
            ):  # 방문하지 않은 인덱스이고 두 정점이 연결되어 있다면 재귀호출
                visited_bfs[i] = 1  # 방문한 인덱스는 1로 표시해줌
                q.append(i)  # deque에 다음 방문할 인덱스가 되도록 현재 방문한 인덱스를 추가


dfs(V)
bfs(V)
