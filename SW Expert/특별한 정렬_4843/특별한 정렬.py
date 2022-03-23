def solve1():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        A = list(map(int, input().split()))

        # 정렬
        A = sorted(A, reverse=True)
        
        # 출력
        idx = 0
        print("#{}".format(t), end=" ")
        while len(A) > idx and idx < 5:
            # res.append(A[idx])
            # res.append(A.pop())
            print(A[idx], end=" ")
            print(A.pop(), end=" ")
            idx+=1
        print()

def solve2():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        A = list(map(int, input().split()))

        # 정렬
        for i in range(len(A)):
            max_num = 0
            for j in range(i, len(A)):
                if max_num < A[j]:
                    max_num = A[j]
                    idx = j
            A[i], A[idx] = A[idx], A[i]
    
        # 출력
        idx = 0
        print("#{}".format(t), end=" ")
        while len(A) > idx and idx < 5:
            # res.append(A[idx])
            # res.append(A.pop())
            print(A[idx], end=" ")
            print(A.pop(), end=" ")
            idx+=1
        print() 

def solve3():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        A = list(map(int, input().split()))

        for i in range(len(A)):
            if i%2 == 0:
                max_idx = find_max_idx(A, i)
                A[i], A[max_idx] = A[max_idx], A[i] # 가장 큰 값과 위치 바꿈
            else:
                min_idx = find_min_idx(A, i)
                A[i], A[min_idx] = A[min_idx], A[i] # 가장 큰 값과 위치 바꿈

        # 출력
        print("#{}".format(t), end=" ")
        for i in range(10):
            print(A[i], end=" ")
        print()

def find_max_idx(A, i):
    max_num = 0
    idx = 0
    for j in range(i, len(A)):
        if max_num < A[j]:
            max_num = A[j]
            idx = j
    return idx

def find_min_idx(A, i):
    min_num = 100+1
    idx = 0
    for j in range(i, len(A)):
        if min_num > A[j]:
            min_num = A[j]
            idx = j
    return idx

if __name__ == "__main__":
    solve3()