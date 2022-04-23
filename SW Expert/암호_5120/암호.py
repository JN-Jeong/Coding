"""
만들어진 비밀번호 숫자 반환
list 반환
"""

def solve():
    N, M, K = map(int, input().split())
    passwords = list(map(int, input().split()))

    idx = 0
    for i in range(K):
        insert_num = passwords[(idx + M - 1) % len(passwords)] + passwords[(idx + M) % len(passwords)]
        if idx + M == len(passwords):
            idx = -1
            passwords.append(insert_num)
        else:
            idx = (idx + M) % len(passwords)
            passwords[idx:idx] = [insert_num] # M칸 뒤에 숫자 삽입
        print("idx : ", idx)
        print(passwords)

    return passwords


if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print("#{}".format(i), end=" ")
        result = solve()
        if len(result) > 10:
            for i in range(len(result)-1, len(result)-10-1, -1):
                print(result[i], end=" ")
        else:
            for i in range(len(result)-1, -1, -1):
                print(result[i], end=" ")
        print()