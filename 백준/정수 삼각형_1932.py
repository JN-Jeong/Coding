'''
삼성노트 '화이트보드용' 노트 참고
'''

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
# print(tri)

for row in range(n-1, 0, -1):
    for col in range(len(tri[row])-1):
        tri[row-1][col] += max(tri[row][col], tri[row][col+1])

print(tri[0][0])