"""
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
"""

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N
def solve(depth, idx): 
    global ans
    if depth == N // 2:     # 스타트팀 완성되었으면 visited에 표시되지 않은 남은 선수들이 링크팀이 됨
        stat1, stat2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] == 1 and visited[j] == 1:
                    stat1 += S[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    stat2 += S[i][j]

        ans = min(ans, abs(stat1 - stat2))
        return

    for i in range(idx, N):
        if visited[i] == 0:
            visited[i] = 1
            print(visited)
            solve(depth + 1, i + 1)
            visited[i] = 0


ans = 9876543210
solve(0, 0)
print(ans)