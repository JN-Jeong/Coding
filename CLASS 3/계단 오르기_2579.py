n = int(input())
stairs = [int(input()) for _ in range(n)]
score = [0] * n
if n > 0:
    score[0] = stairs[0]
if n > 1:
    score[1] = score[0] + stairs[1]
if n > 2:
    for i in range(2, n):
        score[i] = max(score[i-2], score[i-3] + stairs[i-1]) + stairs[i] # + stairs[i] = 마지막 도착 계단
print(score[-1])