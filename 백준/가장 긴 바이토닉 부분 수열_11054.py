'''
10
1 5 2 1 4 3 4 5 2 1

띄엄띄엄 수열이 만들어져도 됨
'''

N = int(input())
A = list(map(int, input().split()))
reverse_A = A[::-1]
print(A, reverse_A)

inc = [1 for _ in range(N)]
dec = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            inc[i] = max(inc[i], inc[j] + 1)
        if reverse_A[i] > reverse_A[j]:
            dec[i] = max(dec[i], dec[j] + 1)

        print(inc, dec)


result = [0 for _ in range(N)]
for i in range(N):
    result[i] = inc[i] + dec[N-i-1] - 1

print(result)
print(max(result))