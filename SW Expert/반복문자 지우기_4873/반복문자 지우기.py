def solve():
    s = input()

    idx = 0
    while idx < len(s)-1:
        if s[idx] == s[idx+1]:
            s = s[:idx] + s[idx+1+1:]
            if idx > 1:
                idx -= 1
                continue
        
        idx += 1
        # print(s)
    
    return len(s)
            

if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))