N = int(input())

def check_end(n):
    if '666' in str(n):
        return True
    
    return False

cnt = 0
i = 666
while cnt <= 10000:
    if check_end(i):
        cnt += 1
    
    if cnt == N:
        print(i)
        break
    
    i += 1