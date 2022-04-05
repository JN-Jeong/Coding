T = int(input())
A = [i for i in range(1, 13)]

for t in range(1, T+1):
    subsets = []
    N, K = map(int, input().split())
    
    # 순열
    for i in range(1<<len(A)): # 모든 부분 집합 만들기
        subset = []
        for j in range(len(A)):
            if i & (1<<j):
                subset.append(j+1)
    
        if len(subset) == N: # 부분 집합의 원소 개수가 N이라면 추가
            subsets.append(subset)

    ans = 0
    for sets in subsets: # 부분 집합의 원소 개수가 N개이고 원소의 합이 K라면 정답
        if sum(sets) == K:
            ans += 1

    print("#{} {}".format(t, ans))