def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(int(a * b / gcd(a, b)))
