n = int(input())
stairs = [int(input()) for _ in range(n)]
print(stairs)

score = [0] * n
if n > 0:
    score[0] = stairs[0]
if n > 1:
    score[1] = score[0] + stairs[1]
if n > 2:
    for i in range(2, n):
        print(i-2, i-3, score)
        score[i] = max(score[i-2], score[i-3] + stairs[i-1]) + stairs[i]    # i가 2일 때 score[i-3]이면 score[-1]이고 값이 0임, + stairs[i] = 마지막 도착 계단

print(score[-1])