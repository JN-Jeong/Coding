N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
print(paper)

zero = 0
one = 0
m_one = 0

def make_P(x, y, N): # 색종이 만들기 문제의 응용 (색종이 만들기는 4방향, 종이의 개수는 9방향)
    global zero
    global one  
    global m_one
    num = paper[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != num:
                make_P(x, y, N//3)
                make_P(x, y+N//3, N//3)
                make_P(x, y+N//3*2, N//3)

                make_P(x+N//3, y, N//3)
                make_P(x+N//3, y+N//3, N//3)
                make_P(x+N//3, y+N//3*2, N//3)
                
                make_P(x+N//3*2, y, N//3)
                make_P(x+N//3*2, y+N//3, N//3)
                make_P(x+N//3*2, y+N//3*2, N//3)
                return
    if num == 0:
        zero += 1
        print(x, y, N)
    elif num == 1:
        one += 1
    elif num == -1:
        m_one += 1

make_P(0, 0, N)
print(m_one)
print(zero)
print(one)
print(9//3*2)