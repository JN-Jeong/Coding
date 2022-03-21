from random import randrange


T = int(input())

for i in range(T):
    N = int(input())
    rectangles = [[""]*10 for _ in range(10)] # map 만듬
    for _ in range(N): # 입력
        row1, column1, row2, column2, color =  (map(int, input().split())) # 입력 받음
        for j in range(row1, row2+1): # 입력받은 크기만큼 반복하며 색칠해줌
            for k in range(column1, column2+1):
                if color == 1:
                    rectangles[j][k] += "R"
                else:
                    rectangles[j][k] += "B"
    
    purple = 0
    for j in range(10):
        for k in range(10):
            if "R" in rectangles[j][k] and "B" in rectangles[j][k]: # 색칠된 부분에 R, B가 동시에 존재한다면 보라색
                purple += 1

    print("#{} {}".format(i+1, purple))