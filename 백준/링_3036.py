def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

N = int(input())
rings = list(map(int, input().split()))

for i in range(1, len(rings)):
    gcd = GCD(rings[0], rings[i])
    print(f"{int(rings[0]/gcd)}/{int(rings[i]/gcd)}")