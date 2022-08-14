N = int(input())

rooms = []
for _ in range(N):
    rooms.append(list(map(int, input().split())))

rooms.sort()
rooms.sort(key=lambda x:x[1])
print(rooms)

answer = 1
temp = rooms[0][1]
for i in range(1, len(rooms)):
    if temp <= rooms[i][0]:
        temp = rooms[i][1]
        answer += 1

print(answer)