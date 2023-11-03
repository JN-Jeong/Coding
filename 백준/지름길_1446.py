"""
1446. 지름길
"""
import heapq


def solution():
    N, D = map(int, input().split())
    graph = [[] for _ in range(D + 1)]

    for i in range(D):
        graph[i].append([i + 1, 1])

    distances = [float("inf")] * (D + 1)
    distances[0] = 0

    for _ in range(N):
        start, end, dis = map(int, input().split())
        if end > D:  # 도착 지점보다 지름길의 도착 지점이 더 멀면 continue
            continue
        graph[start].append([end, dis])

    # print(distances)

    q = []
    heapq.heappush(q, [0, 0])
    while q:
        # print("@", q)
        distance, start = heapq.heappop(q)
        # print("@@", distance, start, graph[start])
        if distances[start] < distance:
            continue

        for g in graph[start]:
            cost = distance + g[1]
            # print("@@@", distances[g[0]], cost)
            if distances[g[0]] > cost:  # 기존 거리가 더 길면 지름길로 갱신
                distances[g[0]] = cost
                heapq.heappush(q, [cost, g[0]])
            # print("@@@@", q)
            # print("@@@@@", distances)

    # print(graph)
    # print(distances)
    print(distances[D])

    return


if __name__ == "__main__":
    solution()
