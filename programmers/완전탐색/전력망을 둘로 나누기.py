"""
하나로 연결되어 있는 전력망
전선을 하나 끊어서 하나였던 전력망을 둘로 나눠야 함

전력망이 두 개이기 때문에 송전탑 하나를 시작으로 연결된 송전탑을 모두 방문하여 한 쪽 전력망의 송전탑 개수를 세면 양쪽 전력망의 송전탑 개수를 알 수 있음
연결되어 있는 전선을 하나씩 끊으면서 완전탐색으로 양쪽 송전탑 개수의 차이를 업데이트 해주어서 차이가 가장 적은 값을 반환
"""


from collections import deque


def solution(n, wires):
    answer = float("inf")

    graph = make_graph(n, wires)
    # print(graph)
    for wire in wires:
        result = search(graph, wire)
        answer = min(answer, abs((n - result) - result))

    return answer


def search(graph, del_wire):
    visited = [0] * len(graph)
    visited[del_wire[0]] = 1  # del_wire[0] : 전선 끊기 (방문하지 않도록 해줌)

    q = deque()
    q.append(graph[del_wire[0]])
    net = 1

    while q:
        connect = q.popleft()

        for i in range(1, len(connect)):
            if connect[i] == 1 and visited[i] == 0 and i != del_wire[1]:  # del_wire[1] : 전선 끊기 (방문하지 않도록 해줌, 큐에 추가 안함)
                visited[i] = 1
                q.append(graph[i])
                net += 1

    print("# : ", net)
    return net


def make_graph(n, wires):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for wire in wires:
        l_wire, r_wire = wire
        graph[l_wire][r_wire] = graph[r_wire][l_wire] = 1

    return graph


nums = [9, 4, 7]
wires = [[[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]], [[1, 2], [2, 3], [3, 4]], [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]]
result = [3, 0, 1]

for n, wire in zip(nums, wires):
    print(solution(n, wire))
