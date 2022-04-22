"""
10개의 숫자 출력
index 필요 -> list 사용
int 반환
"""

"""
제한시간 초과 발생
"""

def solve():
    N, M = map(int, input().split())

    seq_nums = list(map(int, input().split()))
    for _ in range(M - 1):
        temp = list(map(int, input().split()))
        print(seq_nums)
        for i in range(len(seq_nums)):
            if seq_nums[i] > temp[0]:
                seq_nums[i:i] = temp # 특정 index에 리스트 원소들을 삽입하는 방법
                break
        else:
            seq_nums.extend(temp) # 리스트 끝에 temp(iterable)의 모든 원소들을 삽입
    print(seq_nums)

    return seq_nums


if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        result = solve()
        print("#{}".format(i), end=" ")
        for i in range(1, 10+1):
            print("{}".format(result[-i]), end=" ")
        print()