"""
주어진 인덱스 L번째의 데이터를 출력
int 반환
"""

"""
Queue
"""

def solve():
    N, M, L = map(int, input().split())

    seq_nums = list(map(int, input().split()))
    for i in range(M):
        idx, num = map(int, input().split())
        seq_nums.insert(idx, num)

    return seq_nums[L]


if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print("#{} {}".format(i, solve()))