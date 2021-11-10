import sys
M, N = map(int, sys.stdin.readline().split())

def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int((num**0.5)+1)): # 소수인지 확인할 수의 제곱근까지만 학인하면 판별 가능
            if num % i == 0:
                return False
    
    return True

for i in range(M, N+1):
    if is_prime(i):
        print(i)