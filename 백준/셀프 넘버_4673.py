def gen(n):
    temp = n
    while temp > 0:
        one_digit = temp % 10
        temp = temp // 10
        n += one_digit
    return n

results = [0] * 10001
for i in range(10000):
    n = gen(i)
    if n > 10000:
        continue
    results[n] += 1

for i in range(len(results)):
    if results[i] == 0:
        print(i)