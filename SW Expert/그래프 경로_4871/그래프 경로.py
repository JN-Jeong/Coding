from collections import deque

def solve():
    V, E = map(int, input().split()) # 노드 수, 간선 수

    graph = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s][e] = 1
    
    S, G = map(int, input().split())
    # print(graph)

    visited_bfs = [0]*(V+1)
    return bfs(S, G, graph, visited_bfs)

def bfs(S, G, graph, visited_bfs):
    q = deque()
    q.append(S)
    visited_bfs[S] = 1
    while q:
        v = q.popleft()
        for i in range(1, len(graph)):
            if visited_bfs[i] == 0 and graph[v][i] == 1:
                visited_bfs[i] = 1
                q.append(i)
            if visited_bfs[G] == 1: # 목적지 노드를 방문했다면 return 1
                # print(v, i, graph[v][i])
                return 1
        # print(visited_bfs)
 
    return 0

if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))