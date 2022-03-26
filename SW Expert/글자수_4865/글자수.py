def solve():
    str1 = list(input())
    str2 = list(input())

    dic = {}
    for char in str2:
        if char in str1:
            if char not in dic:
                dic[char] = 0
            dic[char] += 1
    
    return max(dic.values())

if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))