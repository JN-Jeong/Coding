N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

answer = 0
temp = prices[0]
for i in range(1, len(prices)):
    answer += temp * distances[i-1]
    temp = min(temp, prices[i])

print(answer)