"""
전선 하나를 끊음 -> permutations으로 n-1개?
"""


from collections import deque
from itertools import permutations


def solution(n, wires):
    answer = float("inf")

    # for wire in wires:
    #     print(wire)

    ids = list(map(list, permutations(range(1, len(wires) + 1), len(wires) - 1)))
    # print(ids)

    for idx in ids:
        # wire = [wires[i] for i in idx]
        # print(wire)
        answer = min(answer, (search(make_graph(n, wires, idx))))

    return answer


def search(graph):

    visited = [0] * len(graph)
    cnt = 0
    result = 0

    for idx in range(1, len(graph)):
        q = deque()
        q.append(idx)
        net = 0

        if visited[idx] == 1:
            continue

        while q:
            i = q.popleft()
            for j in range(1, len(graph)):
                if i != j and graph[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    q.append(j)
                    net += 1

        result = abs(result - net)
        cnt += 1

    return result


def make_graph(n, wire, idx):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for i in idx:
        l_wire, r_wire = wire[i - 1]
        graph[l_wire][r_wire] = graph[r_wire][l_wire] = 1

    return graph


nums = [9, 4, 7]
wires = [[[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]], [[1, 2], [2, 3], [3, 4]], [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]]
result = [3, 0, 1]

for n, wire in zip(nums, wires):
    print(solution(n, wire))
