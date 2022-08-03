'''
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10

0
1
2
1
----------------
'''
## 50점
# S = input()
# q = int(input())
# temp = [{}]
# seqs = {}
# for s in S:
#     if s not in seqs:
#         seqs[s] = 0
#     seqs[s] += 1
#     temp.append(seqs.copy())
# print(temp[6])

# for _ in range(q):
#     a, l, r = input().split()
#     left = 0
#     right = 0
#     if a in temp[int(l)]:
#         print("left : ", temp[int(l)])
#         left = temp[int(l)][a]
    
#     if a in temp[int(r)+1]:
#         print("right : ", temp[int(r)+1])
#         right = temp[int(r)+1][a]
    
#     print(right - left)


# 100점
import sys


S = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

alphabets = [[0] * 26 for _ in range(len(S) + 1)]
alphabets[1][ord(S[0]) - 97] = 1
for i in range(2, len(S) + 1):
    alphabets[i][ord(S[i-1]) - 97] = 1
    for j in range(26):
        alphabets[i][j] += alphabets[i-1][j]

for i in range(q):
    a, l, r = sys.stdin.readline().strip().split()
    print(alphabets[int(r) + 1][ord(a)-97] - alphabets[int(l)][ord(a)-97])