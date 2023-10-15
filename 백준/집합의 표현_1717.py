"""
1717. 집합의 표현
"""
import sys

sys.setrecursionlimit(10**6)


def solution():
    n, m = map(int, sys.stdin.readline().split())

    parents = [0] * (n + 1)
    for i in range(1, len(parents)):
        parents[i] = i

    def find(x):
        if parents[x] != x:
            p = find(parents[x])
            parents[x] = p
            return parents[x]
        return x

    def union(x, y):
        parent_x = find(x)
        parent_y = find(y)

        if parent_x < parent_y:
            parents[parent_y] = parent_x
        else:
            parents[parent_x] = parent_y

    for _ in range(m):
        num, a, b = map(int, sys.stdin.readline().split())
        if num:
            fa = find(a)
            fb = find(b)
            # print("@", fa, fb)
            if fa == fb:
                print("yes")
            else:
                print("no")
        else:
            if a != b:
                union(a, b)

        print(parents)


if __name__ == "__main__":
    solution()
