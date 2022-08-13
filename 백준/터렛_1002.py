from math import sqrt


T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 두 원점 사이의 거리
    # dis = ((abs(x1 - x2))**2 + (abs(y1 - y2))**2) ** 0.5
    dis = sqrt(((abs(x1 - x2))**2 + (abs(y1 - y2))**2))

    # 두 원이 겹친다면 류재명이 있을 수 있는 위치의 개수가 무한대
    if dis == 0 and r1 == r2:
        print(-1)
    # 내접, 외접
    elif dis == abs(r1 - r2) or dis == r1 + r2:
        print(1)
    # 두 원이 서로 다른 두 점에서 만남
    elif abs(r1 - r2) < dis < r1 + r2:
        print(2)
    else:
        print(0)
    