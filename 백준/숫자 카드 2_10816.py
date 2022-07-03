N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_dict = {}
for n in N_list:
    if n not in N_dict:
        N_dict[n] = 0
    N_dict[n] += 1

for m in M_list:
    if m in N_dict:
        print(N_dict[m], end = ' ')
    else:
        print(0, end = ' ')