"""
최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 반환
연결되지 않았다면 0 반환
int 반환
"""

from collections import deque


def solve():
    V, E = map(int, input().split())
    global graph
    graph = [[0] * (V+1) for _ in range(V+1)]
    
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = graph[j][i] = 1
    
    S, G = map(int, input().split())

    print(graph)

    global visited_bfs
    visited_bfs = [0] * (V+1)

    return bfs(S, G)

def bfs(S, G):
    q = deque()
    q.append((S, 1))

    while q:
        node, num = q.popleft()
        visited_bfs[node] = 1

        for i in range(len(graph)):
            if visited_bfs[i] == 0 and graph[node][i] == 1:
                if i == G:
                    return num
                q.append((i, num + 1))
            print(q)
    
    return 0

if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print("#{} {}".format(i, solve()))