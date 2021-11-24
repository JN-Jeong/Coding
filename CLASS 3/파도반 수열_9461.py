T = int(input())

for _ in range(T):
    N = int(input())
    tri = [1,1,1,2,2]
    for i in range(5, N):
        tri.append(tri[i-3] + tri[i-2])
    if N < 4:
        print(1)
    elif N < 6:
        print(2)
    else:
        print(tri[-1])