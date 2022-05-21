N = int(input())

# i = 2
# while N >= 0 and N >= i:
#     if N % i == 0:
#         print(i)
#         N = N // i
#     else:
#         i += 1


for i in range(2, int(N ** 0.5) + 1):
    while N % i == 0:
        print(i)
        N //= i

if N > 1:
    print(N)