K = int(input())
buildings = list(map(int, input().split()))
visited = [[] for _ in range(K)]

def Tree(arr, idx):
    mid = len(arr) // 2
    visited[idx].append(arr[mid])

    if len(arr) <= 1:
        return

    Tree(arr[:mid], idx + 1)
    Tree(arr[mid + 1:], idx + 1)

Tree(buildings, 0)

for i in range(K):
    print(*visited[i]) # 2차원 리스트의 행 전체를 출력하는 방법
