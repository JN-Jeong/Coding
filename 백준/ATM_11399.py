N = int(input())
P = list(map(int, input().split()))

P.sort()
print(P)
memo = [0] * N
memo[0] = P[0]
for i in range(1, len(P)):
    memo[i] = memo[i-1] + P[i]

print(memo)
print(sum(memo))