from collections import deque


def get_points(v, N):
    lst = []
    if v[0] > 0:
        lst.append([v[0] - 1, v[1]])
    if v[1] > 0:
        lst.append([v[0], v[1] - 1])
    if v[1] < N - 1:
        lst.append([v[0], v[1] + 1])
    if v[0] < N - 1:
        lst.append([v[0] + 1, v[1]])

    return lst


def bfs(sea, loc, w, N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[loc[0]][loc[1]] = True
    sea[loc[0]][loc[1]] = 0
    eat = []
    min_dist = 10000
    q = deque([[loc, 0]])
    while q:
        v, dist = q.popleft()
        if dist < min_dist:
            for i in get_points(v, N):
                if not visited[i[0]][i[1]]:
                    if sea[i[0]][i[1]] in [0, w]:
                        q.append([i, dist + 1])

                    elif sea[i[0]][i[1]] < w:
                        min_dist = dist + 1
                        eat.append(i)

                    visited[i[0]][i[1]] = True

    return eat, min_dist


N = int(input())
sea = []
baby = []
weight = 2
for i in range(N):
    tmp = list(map(int, input().split()))
    if not baby:
        for j in range(N):
            if tmp[j] == 9:
                baby = [i, j]
    sea.append(tmp)

t = 0
count = 0
while True:
    lst, dist = bfs(sea, baby, weight, N)
    if lst:
        lst.sort()
        baby = lst[0]
        count += 1
        if count == weight:
            count = 0
            weight += 1
        t += dist
    else:
        break

print(t)


# import sys
# from collections import deque

# import numpy as np

# input = sys.stdin.readline

# # 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# # 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

# n = int(input())
# space = [list(map(int, input().split())) for _ in range(n)]

# # 상, 하, 좌, 우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# cnt = 0

# # 아기 상어 좌표 초기화
# x, y, size = 0, 0, 2
# for i in range(n):
#     for j in range(n):
#         if space[i][j] == 9:
#             x = i
#             y = j


# # 4
# # 4 3 2 1
# # 0 0 0 0
# # 0 0 9 0
# # 1 2 3 4
# def bfs(x, y, shark_size):
#     distance = [[0] * n for _ in range(n)]
#     visited = [[0] * n for _ in range(n)]

#     # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때,
#     # 지나야 하는 칸의 개수의 최솟값이다. (bfs)
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = 1
#     temp = []
#     while q:
#         print("q: ", q)
#         print("visited: ", np.array(visited), sep="\n")
#         print("distance: ", np.array(distance), sep="\n")
#         curr_x, curr_y = q.popleft()
#         for i in range(4):
#             nx = curr_x + dx[i]
#             ny = curr_y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
#                 # 크기가 같으면 지나갈 수는 있음
#                 if space[nx][ny] <= shark_size:
#                     q.append((nx, ny))
#                     # print('visited: ', np.array(visited), sep='\n')
#                     visited[nx][ny] = 1
#                     # print('distance: ', np.array(distance), sep='\n')
#                     distance[nx][ny] = distance[curr_x][curr_y] + 1
#                     if space[nx][ny] < shark_size and space[nx][ny] != 0:
#                         # 자신보다 작은 물고기만 먹을 수 있음
#                         temp.append((nx, ny, distance[nx][ny]))
#                         print("temp origin: ", temp)

#     # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
#     # 물고기가 여러 마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
#     print("temp: ", temp)
#     answer = sorted(temp, key=lambda x: (x[2], x[0], x[1]))
#     print("bfs: ", answer)
#     return answer


# cnt = 0
# result = 0

# while True:
#     shark = bfs(x, y, size)
#     # 더 이상 먹을 수 있는 물고기가 공간에 없다면,
#     # 아기 상어는 엄마 상어에게 도움을 요청한다.
#     if len(shark) == 0:
#         break
#     # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
#     # 그러한 물고기가 여러 마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
#     # 정렬한 결과를 반영해준다.

#     nx, ny, distance = shark.pop(0)

#     # 움직이는 칸수가 곧 시간이 된다.
#     result += distance
#     # 상어가 자리를 옮겼으니 0, 물고기를 먹었으니 0
#     space[x][y], space[nx][ny] = 0, 0

#     # 상어 좌표를 먹은 물고기 좌표로 옮겨준다.
#     x, y = nx, ny
#     cnt += 1
#     # 상어의 성장
#     if cnt == size:
#         size += 1
#         cnt = 0
#     print("count: ", cnt)
#     print("size:", size)

# print(result)
# print(space)
