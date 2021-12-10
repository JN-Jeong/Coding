N = int(input())
X = list(map(int, input().split()))

set_X = {}
idx = 0
for i in sorted(X):
    if not i in set_X:
        set_X[i] = idx
        idx += 1

for i in X:
    print(set_X[i], end=' ')