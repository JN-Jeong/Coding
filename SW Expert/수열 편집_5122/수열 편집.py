"""
I 명령어는 insert
D 명령어는 delete
C 명령어는 change
완성된 수열의 인덱스 L 번째 값
int 반환
"""


def solve():
    N, M, L = map(int, input().split())
    seqs = list(map(int, input().split()))
    
    for i in range(M):
        command = input().split()
        if command[0] == "I":
            seqs[int(command[1]):int(command[1])] = [int(command[2])]
        elif command[0] == "D":
            seqs.pop(int(command[1]))
        elif command[0] == "C":
            seqs[int(command[1])] = int(command[2])

    if len(seqs)-1 >= L:
        return seqs[L]
    else:
        return -1


if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print("#{} {}".format(i, solve()))