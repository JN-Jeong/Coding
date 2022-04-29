def solve():
    N = int(input())

    arr = [i for i in range(1, N+1)]
    print(arr)

    global trees
    trees = [0] * (N+1)
    tree(1, N)
    print(trees) # [0, 4, 2, 6, 1, 3, 5]
                 # [0, 5, 3, 7, 2, 4, 6, 8, 1]
                 # [0, 8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

    return trees[1], trees[N//2]
    
def tree(idx, N):
    global trees
    global count

    if idx <= N: 
        tree(idx*2, N) # 왼쪽 노드 값을 채움
        trees[idx] = count
        print(idx)
        count += 1
        tree(idx*2+1, N) # 오른쪽 노드 값을 채움

if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        count = 1
        root, node = solve()
        print(f"#{i} {root} {node}")