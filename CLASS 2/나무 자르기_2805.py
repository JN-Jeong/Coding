import sys
N, M = map(int, sys.stdin.readline().split())
trees = sys.stdin.readline().split()
trees = [int(i) for i in trees]

start = 0
end = max(trees)
res = []
while start <= end:
    mid = (start + end) // 2
    length = 0
    for tree in trees:
        if mid < tree:
            length += tree - mid
            print(length)
    
    if length >= M:
        res.append(mid)
        start = mid + 1
    else:
        end = mid - 1
print(max(res))