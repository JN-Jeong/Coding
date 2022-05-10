n1 = int(input())
n2 = int(input())

n = n2
for i in range(3):
    one_digit = n % 10
    n = n // 10
    print(n1 * one_digit)

print(n1 * n2)