def is_prime(n):
    if n == 1:
        return False
    
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    
    return True


M = int(input())
N = int(input())

result = 0
min_ = N+1
for i in range(M, N+1):
    if is_prime(i):
        result += i
        if min_ > i:
            min_ = i

if result and min_:
    print(result)
    print(min_)
else:
    print(-1)