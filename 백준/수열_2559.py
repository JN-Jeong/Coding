N, K = list(map(int, input().split()))
temperature = list(map(int, input().split()))

temp = [0]
for i in range(N):
    temp.append(temp[i] + temperature[i])

print(temp)

res = -987  # 범위가 -100 ~ 100
for i in range(K, len(temp)):
    res = max(res, temp[i] - temp[i-K])

print(res)