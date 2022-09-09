N = int(input())
X = list(map(int, input().split()))

set_X = {}
idx = 0
for i in sorted(X):  # 정렬된 X 리스트의 변수들에 오름차순으로 번호를 부여한다
    if not i in set_X:
        set_X[i] = idx
        idx += 1

for i in X:
    print(set_X[i], end=" ")
