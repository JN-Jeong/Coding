N = int(input())

time = []
for _ in range(N):
    time.append(list(map(int, input().split())))

res = []
time = sorted(time)
time = sorted(time, key=lambda x:x[1])
# => time = sorted(time, key = lambda x : (x[1], x[0])) # 왜 순서가 바뀌는지는 모르겠음...
end = time[0][1]
max_meeting = 1
for i in range(1, len(time)):
    if end <= time[i][0]:
        end = time[i][1]
        max_meeting += 1
        print(time[i])
    res.append(max_meeting)

print(time)
print(max_meeting)
print(res)
print(max(res))