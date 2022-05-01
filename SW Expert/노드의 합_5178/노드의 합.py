def solve():
    N, M, L = map(int, input().split())
    leaf_nodes = []

    for _ in range(M):
        leaf_nodes.append(tuple(map(int, input().split())))
    print(leaf_nodes)

    tree = [0] * (N+1)
    for idx, value in leaf_nodes:
        tree[idx] = value
    
    print(tree)

    for i in range(len(tree)-1, -1, -1):
        if tree[i] == 0:
            try:
                tree[i] = tree[i*2] + tree[i*2+1]
            except:
                tree[i] = tree[i*2]
    
    print(tree)

    return tree[L]


if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print(f"#{i} {solve()}")