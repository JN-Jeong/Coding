N, M = map(int, input().split())

pw_dict = {}
for _ in range(N):
    addr, pw = input().split()
    pw_dict[addr] = pw

for _ in range(M):
    addr = input()
    print(pw_dict[addr])