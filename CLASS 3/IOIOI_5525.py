N = int(input())
M = int(input())
S = input()

Pn = 'I'
for _ in range(N):
    Pn += 'OI'

l = len(Pn)
num = 0
for i in range(0, M-l):
    print(S[i:i+l])
    if S[i:i+l] == Pn:
        num += 1

print(num)