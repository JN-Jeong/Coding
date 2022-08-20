a, b = map(int, input().split())

# 최대공약수
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
print(gcd(a, b))

# 최소공배수
print(int(a * b / gcd(a, b)))