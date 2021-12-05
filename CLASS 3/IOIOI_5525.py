import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

num = 0
count = 0
i = 1
while i < len(S)-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        count += 1
        if count >= N:
            num += 1
        i += 2
    else:
        count = 0
        i += 1
    
print(num)