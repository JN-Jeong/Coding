import sys
N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0]
for i in range(len(num_list)):
    sum_list.append(sum_list[i] + num_list[i])

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_list[j] - sum_list[i-1])