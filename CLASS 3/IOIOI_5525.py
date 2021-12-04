import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

S = S.split('I')

num = 0
for i in range(len(S)-N):
    for j in range(i, i+N):
        if S[j] != 'O':
            break
        elif j == i+N-1:
            num += 1

print(num)