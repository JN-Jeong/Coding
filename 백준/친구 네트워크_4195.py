"""
합 집합 찾기(Union-Find) 알고리즘
"""
def find_parent(x):
    if x == parent[x]:  # x가 실질적인 부모라면 x 반환
        return x
    else:               # x가 실질적인 부모가 아니라면 재귀 함수 호출
        p = find_parent(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    parent[y] = x

parent = []

for i in range(0, 5):
    parent.append(i)

union(1, 4)
union(2, 4)

for i in range(1, len(parent)):
    print(find_parent(i), end = ' ')


# 패캠 강의 풀이
if __name__ == '__main__':
    T = int(input())
    
    def find_parent(x): # x의 parent를 반환
        if x == parent[x]:
            return x
        else:
            p = find_parent(parent[x])
            parent[x] = p
            return parent[x]

    def union(x, y): 
        x = find_parent(x)
        y = find_parent(y)

        if x != y:
            parent[y] = x           # y의 부모를 x로 설정
            number[x] += number[y]  # x와 y의 친구 관계 수를 더하여 부모가 된 x에 저장

    for _ in range(T):
        parent = dict()
        number = dict()

        f = int(input())

        for _ in range(f):
            x, y = input().split()

            if x not in parent:
                parent[x] = x
                number[x] = 1
            if y not in parent:
                parent[y] = y
                number[y] = 1

            print("union 전 : ", parent)
            union(x, y)
            print("union 후 : ", parent)

            print(number[find_parent(x)])
