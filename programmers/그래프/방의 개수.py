from collections import defaultdict


def movement(n, node):
    if n == 0:
        return [node[0], node[1] + 1]
    elif n == 1:
        return [node[0] + 1, node[1] + 1]
    elif n == 2:
        return [node[0] + 1, node[1]]
    elif n == 3:
        return [node[0] + 1, node[1] - 1]
    elif n == 4:
        return [node[0], node[1] - 1]
    elif n == 5:
        return [node[0] - 1, node[1] - 1]
    elif n == 6:
        return [node[0] - 1, node[1]]
    else:
        return [node[0] - 1, node[1] + 1]


def solution(arrows):
    graph = defaultdict(set)
    pre = [0, 0]
    for arrow in arrows:
        cnt = movement(arrow, pre)
        mid = [(pre[0] + cnt[0]) / 2, (pre[1] + cnt[1]) / 2]
        graph[tuple(pre)].add(tuple(mid))
        graph[tuple(mid)].add(tuple(pre))
        graph[tuple(mid)].add(tuple(cnt))
        graph[tuple(cnt)].add(tuple(mid))

        pre = cnt

    return 1 - len(graph) + sum(len(i) for i in graph.values()) // 2
