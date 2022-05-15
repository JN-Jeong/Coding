N = int(input())

K = 1
t = 0
while N > 0:
    t += 1
    if N < K:
        K = 1
    N -= K
    K += 1
    
print(t)