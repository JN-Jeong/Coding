N = int(input())
time = list(map(int, input().split()))

min_time = 0
temp = 0
for i in sorted(time):
    temp += i
    min_time += temp
print(min_time)
