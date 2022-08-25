"""
중위순회를 이용하면 X축을 기준으로 왼쪽부터 방문한다는 특징이 있음
중위순회로 탐색하면서 level(깊이)값을 저장
"""

# 패캠 강의 풀이
class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node

def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)
    level_min[level] = min(level_min[level], x)     # 가장 왼쪽에 있는 변수를 찾음
    level_max[level] = max(level_max[level], x)     # 가장 오른쪽에 있는 변수를 찾음
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)


n = int(input())
tree = {}
level_min = [n]     # 최소는 너비가 가장 클 수 있는 값으로 N을 넣어서 초기화
level_max = [0]     # 최대는 너비가 가장 작을 수 있는 값으로 0을 넣어서 초기화
root = -1
x = 1
level_depth = 1

for i in range(1, n + 1):   # 노드의 개수만큼 존재하도록 level과 노드들을 초기화
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = number     # 왼쪽 자식의 parent로 현재의 number를 넣어줌
    if right_node != -1:
        tree[right_node].parent = number    # 오른쪽 자식의parent로 현재의 number를 넣어줌
                                            # 결과적으로 parent값을 -1로 초기화 해줬기 때문에 parent값이 -1인 노드가 루트가 됨

for i in range(1, n + 1):                   # parent값이 -1인 노드가 루트가 되므로 루트가 되는 노드 값을 root에 저장
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)                     # 루트 노드부터 중위순회 진행

result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1):             # 모든 level에 대해서 너비 값을 구함
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)
