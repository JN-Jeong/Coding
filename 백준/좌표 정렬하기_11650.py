N = int(input())

locs = []
for i in range(N):
    x, y = input().split()
    locs.append((int(x), int(y)))

locs.sort()     # key 값을 주지 않으면 x[0], x[1], x[2] ... 차례로 모두 정렬
                # key 값을 lambda x : x[0] 으로 주면 x[0]을 기준으로만 정렬하고 나머지는 stable

for x, y in locs:
    print(f"{x} {y}")