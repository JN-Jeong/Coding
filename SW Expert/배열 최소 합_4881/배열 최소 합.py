# list 자료형은 solve()에 global로 한번 선언해줘도 됨
# int 자료형은 solve()와 dfs()에서 모두 선언해줘야 됨

def solve():
    N = int(input())
    
    global maps
    maps = [list(map(int, input().split())) for _ in range(N)]
    
    global min_sum
    min_sum = 987654321
    
    global visited_dfs
    visited_dfs = [1] * N
    
    dfs(0, 0, N)
    return min_sum

def dfs(idx, sum_, N):
    global min_sum
    if idx == N:
        if sum_ < min_sum:
            min_sum = sum_
        return
    
    # 가지치기(이미 최소합보다 합이 크다면 계산안함)
    if sum_ >= min_sum:
        return
    
    for i in range(N):
        if visited_dfs[i]:
            visited_dfs[i] = 0
            dfs(idx+1, sum_ + maps[idx][i], N)
            visited_dfs[i] = 1

if __name__ == "__main__":
    T = int(input())    
    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))