def solve():
    N = int(input()) // 10
    case = [1, 3]
    for i in range(2, N):
        case.append(case[i-2]*2 + case[i-1])
    
    return case[-1]

if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))