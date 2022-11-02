"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열 길이 구하기
int 반환
DP 문제라고 함
index 필요 없음
"""


def solve():
    A_size = int(input())
    A = list(map(int, input().split()))
    memo = [1] * A_size
    print(memo)

    for i in range(A_size):
        for j in range(i):
            if A[i] > A[j]:
                if memo[i] <= memo[j]:
                    memo[i] = memo[j] + 1
                print(i, j)
                print("memo : ", memo[i], memo[j])

    return max(memo)


if __name__ == "__main__":
    print(solve())
