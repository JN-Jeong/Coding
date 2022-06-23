N = int(input())

n = 2
memo = [0] * 3
memo[1] = 1
memo[2] = 2
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    while n < N:
        memo[1], memo[2] = memo[2], (memo[1] + memo[2]) % 15746
        n += 1
    
    print(memo[-1])