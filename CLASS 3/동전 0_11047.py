N, K = map(int, input().split())
coins = []
for _ in range(N):
    coin = int(input())
    if coin > K:
        continue
    coins.append(coin)

count = 0
while K > 1:
    for i in range(len(coins)-1, -1, -1):
        temp = K // coins[i]
        K = K  % coins[i]
        count += temp

print(count)