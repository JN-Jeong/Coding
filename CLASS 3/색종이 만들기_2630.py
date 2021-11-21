N = int(input())

CP = [list(map(int, input().split())) for _ in range(N)]
cut_CP = []

def make_CP(x, y, N):
    color = CP[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != CP[i][j]:
                make_CP(x, y, N//2)
                make_CP(x+N//2, y, N//2)
                make_CP(x, y+N//2, N//2)
                make_CP(x+N//2, y+N//2, N//2)
                return
    cut_CP.append(color)

make_CP(0, 0, N)
print(cut_CP.count(0))
print(cut_CP.count(1))