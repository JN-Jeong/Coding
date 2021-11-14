N, M = map(int, input().split())

name_dict = {}
doodbo = []
for _ in range(N+M):
    name = input()
    if not name in name_dict:
        name_dict[name] = 0
    name_dict[name] += 1
    
    if name_dict[name] > 1:
        doodbo.append(name)

doodbo = sorted(doodbo)
print(len(doodbo))
for name in doodbo:
    print(name)