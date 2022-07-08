N = int(input())

rooms = []
for _ in range(N):
    rooms.append(list(map(int, input().split())))

rooms.sort()
print(rooms)