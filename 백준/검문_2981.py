"""
입력받은 수들을 오름차순 정렬하고
list[i] - list[i - 1] 값들을 리스트로 따로 만들어줌
이렇게 만든 리스트 내의 값들의 최대공약수의 약수가 구하려는 M이 됨
"""

def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

N = int(input())
nums = sorted([int(input()) for _ in range(N)])
re_nums = []
for i in range(1, N):
    re_nums.append(nums[i] - nums[i - 1])

print(nums)
print(re_nums)

gcd = re_nums[0]
for i in range(1, len(re_nums)):
    gcd = GCD(gcd, re_nums[i])

result = set()
for i in range(2, int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        result.add(i)
        result.add(gcd // i)

result.add(gcd)
print(gcd)
for n in sorted(result):
    print(n, end = ' ')