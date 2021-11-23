T = int(input())

def facto(n):
    if n < 2:
        return 1
    return n * facto(n-1)

for _ in range(T):
    n = int(input())
    clothes_type = {}
    for _ in range(n):
        type_ = input().split()[1]
        if not type_ in clothes_type:
            clothes_type[type_] = 0
        clothes_type[type_] += 1
    case = 1
    for i in clothes_type.values():
        case = case * (i+1)
    print(case-1)