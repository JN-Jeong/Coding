n, k = map(int, input().split())

ans = 1
for i in range(k):
    ans *= n
    n -= 1

div = 1
for i in range(2, k+1):
    div *= i

print((ans // div) % 10007)