def isHansu(n):
    if int(n) < 10:
        return True

    m = int(n[0]) - int(n[1])
    for i in range(1, len(n)-1):
        if int(n[i]) - int(n[i+1]) != m:
            return False
    return True

N = input()
result = 0
if int(N) < 10:
    print(int(N))
else:
    for i in range(1, int(N)+1):
        if isHansu(str(i)):
            result += 1
    print(result)