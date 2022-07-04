n = int(input())

drinks = [int(input()) for _ in range(n)]
print(drinks)

memo = [0] * n

if n > 0:
    memo[0] = drinks[0]
if n > 1:
    memo[1] = drinks[0] + drinks[1]
if n > 2:
    for i in range(2, n):
        memo[i] = max(memo[i-1], memo[i-2] + drinks[i], memo[i-3] + drinks[i-1] + drinks[i])

print(memo[-1])