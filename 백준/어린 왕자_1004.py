"""
시작점, 도착점이 포함되는 원 개수를 구하면 됨
"""

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    count = 0
    for _ in range(n):
        x, y, r = map(int, input().split())
        dis1 = ((x1 - x)**2 + (y1 - y)**2) ** 0.5
        dis2 = ((x2 - x)**2 + (y2 - y)**2) ** 0.5

        if dis1 < r and dis2 < r:   # 시작점과 도착점이 모두 포함된 원이라면 pass
            pass
        elif dis1 < r:
            count += 1
        elif dis2 < r:
            count += 1

    print(count)