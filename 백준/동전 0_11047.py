N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input())) # 오름차순으로 주어짐

answer = 0
while K > 1:
    for i in range(len(coins)-1, -1, -1):
        num1 = K // coins[i] # coin이 필요한 최대 개수
        K = K % coins[i] # 남은 거스름돈
        answer += num1

print(answer)
