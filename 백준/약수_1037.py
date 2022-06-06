N = int(input())
divs = list(map(int, input().split()))

print(sorted(divs))
divs.sort()

if len(divs) > 1:
    print(divs[0] * divs[-1])
else:
    print(divs[0] ** 2)