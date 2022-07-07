# 에라토스테네스의 체
eratos = [1] * (2 * 123456 + 1) # 1 ≤ n ≤ 123,456
eratos[0] = 0
eratos[1] = 0

for i in range(2, int(len(eratos)**0.5) + 1):
    if eratos[i]:
        for j in range(i*2, len(eratos), i):
            eratos[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(sum(eratos[n+1:(2*n)+1]))