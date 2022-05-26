import math


N, W, H = map(int, input().split())

for _ in range(N):
    length = int(input())
    dig = math.sqrt(W**2 + H**2)
    if length <= max(dig, W, H):
        print('DA')
    else:
        print('NE')
