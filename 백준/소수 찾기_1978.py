def is_prime(n):
    if n == 1:
        return False
    
    else:
        for i in range(2, int(n**0.5) + 1):     # 소수인지 확인할 수의 제곱근까지만 학인하면 판별 가능
            if n % i == 0:
                return False
    
    return True

N = int(input())
nums = list(map(int, input().split()))

result = 0
for n in nums:
    if is_prime(n):
        result += 1

print(result)