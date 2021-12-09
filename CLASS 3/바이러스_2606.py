n = int(input())
connect = int(input())
net = [[]*n for _ in range(n+1)]

for _ in range(connect):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

print(net) # 각 index번 컴퓨터에 연결된 컴퓨터 번호가 저장됨

cnt = 0
visited = [0]*(n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in net[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(1)
print(cnt)