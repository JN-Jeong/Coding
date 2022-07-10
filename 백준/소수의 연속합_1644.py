N = int(input())

# 에라토스테네스의 체
eratos = [1] * (N + 1)
eratos[0] = 0
eratos[1] = 0

for i in range(2, int(len(eratos) ** 0.5) + 1):
    if eratos[i]:
        for j in range(i*2, len(eratos), i):
            eratos[j] = 0

primes = []
for i in range(len(eratos)):
    if eratos[i] == 1:
        primes.append(i)

left = 0
right = 0
sum_ = 0
result = 0
while True:
    if sum_ >= N:
        if sum_ == N:
            result += 1
            # print(primes[left:right])
        sum_ -= primes[left]
        left += 1
    elif right == len(primes):
        break
    elif sum_ < N:
        sum_ += primes[right]
        right += 1

print(result)