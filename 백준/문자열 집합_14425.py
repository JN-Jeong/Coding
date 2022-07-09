N, M = map(int, input().split())
S = {}
for _ in range(N):
    s = input()
    if s not in S:
        S[s] = 1

check_S = []
for _ in range(M):
    check_S.append(input())

result = 0
for s in check_S:
    if s in S:
        result += 1

print(result)