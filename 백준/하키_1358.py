W, H, X, Y, P = map(int, input().split())
r = H/2

count = 0
for _ in range(P):
    x, y = map(int, input().split())

    # print((abs(x - X)**2 + abs(y - (Y+r))**2) ** 0.5)
    # print((abs(x - X+W)**2 + abs(y - (Y+r))**2) ** 0.5)
    if X <= x <= X+W and Y <= y <= Y+H: # 선수가 직사각형 안에 있음
        print("x, y : ", x,y)
        count += 1
    elif (abs(x - X)**2 + abs(y - (Y+r))**2) ** 0.5 <= r:   # 선수가 왼쪽 원 안에 있음
        print("x, y : ", x,y)
        count += 1
    elif (abs(x - (X+W))**2 + abs(y - (Y+r))**2) ** 0.5 <= r:   # 선수가 오른쪽 원 안에 있음
        print("x, y : ", x,y)
        count += 1

print(count)
    