import math


def solution():
    answer = 0
    N = int(input())
    A = list(map(int, input().split()))  # 각 시험장 응시자 수
    B, C = map(int, input().split())  # 총감독관 감독 가능한 수, 부감독관 감독 가능한 수

    for i in range(len(A)):
        answer += 1
        A[i] -= B

        if A[i] > 0:
            answer += math.ceil(A[i] / C)

    return answer


if __name__ == "__main__":
    print(solution())
