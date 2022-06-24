N = int(input())

builds = [list(map(int, input().split())) for _ in range(N)]

for i in range(len(builds)):
    rank = 1
    for j in range(len(builds)):
        if builds[i][0] < builds[j][0] and builds[i][1] < builds[j][1]:
            rank += 1
    print(rank, end=' ')