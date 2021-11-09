# PyPy3로 제출

import sys
N, M, B = map(int, sys.stdin.readline().split())

list_map = []
for _ in range(N):
    temp = [int(i) for i in sys.stdin.readline().split()]
    list_map.append(temp)

time = 2**1000 # 걸린 시간 (큰 시간으로 초기화)
height = 0 # 높이

for h in range(0, 256 + 1): # 최대 높이 256까지 반복 (목표 높이)
    in_block = 0
    out_block = 0
    for i in range(N):
        for j in range(M):
            if h < list_map[i][j]: # 현재 높이가 목표 높이보다 크다면 
                in_block += list_map[i][j] - h # 블록을 제거하여 인벤토리에 넣음
            else: # 현재 높이가 목표 높이보다 작다면 
                out_block += h - list_map[i][j] # 블록을 꺼내어 놓음

    if B + in_block - out_block < 0: # 블록의 수가 부족하면 continue
        continue

    temp_time = in_block * 2 + out_block
    if temp_time <= time:
        time = temp_time
        height = h

print(time, height)