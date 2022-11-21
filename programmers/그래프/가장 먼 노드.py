def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distances = [0] * (n + 1)
    visited = [0] * (n + 1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)

    q = [1]
    visited[1] = 1

    while q:
        i = q.pop(0)

        for j in graph[i]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)
                distances[j] = distances[i] + 1

    print(distances)
    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer


n = [6]
vertexs = [
    [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]],
]
returns = [3]

for num, vertex in zip(n, vertexs):
    print(solution(num, vertex))
