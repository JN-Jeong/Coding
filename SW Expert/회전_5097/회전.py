from collections import deque

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    series = list(map(int, input().split()))
    
    series = deque(series)
    for j in range(M):
        series.append(series.popleft())
    
    print("#{} {}".format(i, series[0]))