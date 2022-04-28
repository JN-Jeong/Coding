"""
부모 노드 : i // 2
왼쪽 자식 노드 : 2i
오른쪽 자식 노드 : 2i+1
"""

# def solve():
#     E, N = input().split()
#     E = int(E)
#     arr = input().split()
#     print(arr)

#     trees = [0] * (2**E+1)
#     trees[1] = arr[0]

#     for i in range(E):
#         if arr[2*i] in trees:
#             idx = trees.index(arr[2*i])
#             if trees[2*idx] == 0:
#                 trees[2*idx] = arr[2*i+1]
#             else:
#                 trees[2*idx+1] = arr[2*i+1]
#     print(trees)

#     idx = trees.index(N)
#     childs = [trees[idx]]

#     idx *= 2
#     while idx < len(trees)-1:
#         if trees[idx] != 0:
#             childs.append(trees[idx])
#         if trees[idx+1] != 0:
#             childs.append(trees[idx+1])
#         idx *= 2

#     print(childs)
#     return len(childs)


def solve():
    E, N = map(int, input().split())
    E = int(E)
    arr = list(map(int, input().split()))
    print(arr)

    global left
    global right
    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(E):
        if left[arr[2 * i]] == 0:
            left[arr[2 * i]] = arr[2 * i + 1]
        else:
            right[arr[2 * i]] = arr[2 * i + 1]
        
    print(left)
    print(right)
    inorder(N)

def inorder(node):
    global child
    global left
    global right
    if node == 0:
        return
    
    child += 1
    inorder(left[node])
    inorder(right[node])

if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        global child
        child = 0
        solve()
        print(f"#{i} {child}")