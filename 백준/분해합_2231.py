N = int(input())

def solve(n):
    result = n
    for _ in range(len(str(n))):
        result += n % 10
        n //= 10

    return result

result = 0
for i in range(N-1):
    if solve(i) == N:
        print(i)
        break

else:
    print(0)