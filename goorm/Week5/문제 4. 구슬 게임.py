# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)


def solution():
    global N, M, K, visited
    N, M, K = map(int, input().split())
    visited = defaultdict()

    return ball_game(N, 0)


def ball_game(cur, cnt):
    global N, M, K, visited
    key = str([cur, cnt])
    if key in visited:
        return visited[key]
    elif cur == 0 or cur == N + M:
        return 1
    elif cnt == K:
        return 0

    result = 0
    result += ball_game(cur + 1, cnt + 1)
    result += ball_game(cur, cnt + 1)
    result += ball_game(cur - 1, cnt + 1)

    print(visited)
    result %= 100000007
    visited[key] = result
    return result


if __name__ == "__main__":
    print(solution())
