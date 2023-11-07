"""
프로그래머스 : 이진 변환 반복하기
"""


def solution(s):
    answer = [0, 0]

    while True:
        zero = s.count("0")
        one = s.count("1")
        s = "1" * one
        s = str(bin(len(s)))[2:]
        # print(s)
        answer[0] += 1
        answer[1] += zero

        if s == "1":
            break
    return answer


if __name__ == "__main__":
    seqs = ["110010101001", "01110", "1111111"]
    result = [[3, 8], [3, 3], [4, 1]]

    for i, data in enumerate(seqs):
        s = data
        print(f"#{i}", solution(s))
