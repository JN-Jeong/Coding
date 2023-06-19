# def solution():
#     X, Y = map(int, input().split())
#     diff = Y - X
#     ids = [0] * (diff)
#     ids[0], ids[1] = 1, 2

#     now_num = 3  # 현재 값
#     rep = 2  # 현재 값 반복 횟수
#     chk = 0  # 2번 반복했는지 체크 (chk가 2 되면 rep 증가)
#     idx = 0
#     for i in range(2, diff):
#         if chk != 0 and chk % 2 == 0:
#             rep += 1
#         if idx != 0 and idx % rep == 0:
#             chk += 1
#             now_num += 1
#             idx = 0

#         ids[i] = now_num
#         idx += 1

#     print(ids[-1])


def solution():
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        n = int((b - a) ** 0.5)
        if n**2 == b - a:
            print(2 * n - 1)
        else:
            z = (b - a) - n**2
            if z <= n:
                print(2 * n)
            else:
                print(2 * n + 1)


if __name__ == "__main__":
    solution()


"""
1
1 - 1

2
1 1 - 2

3
1 1 1 - 3

4
1 2 1 - 3

5
1 2 1 1 - 4

6
1 2 2 1 - 4

7
1 2 2 1 1 - 5

8
1 2 2 2 1 - 5

9
1 2 3 2 1 - 5

10
1 2 2 2 2 1 - 6

11
1 2 3 2 2 1 - 6

12
1 2 3 3 2 1 - 6

13
1 2 3 3 2 1 1 - 7

14
1 2 3 3 2 2 1 - 7

15
1 2 3 4 3 1 1 - 7

16
1 2 3 4 3 2 1 - 7

17
1 2 3 4 3 2 1 1 - 8

18
1 2 3 4 3 2 2 1 - 8

19
1 2 3 4 3 3 2 1 - 8

20
1 2 3 4 4 3 2 1 - 8

21
1 2 3 4 4 3 2 1 1 - 9

22
1 2 3 4 4 3 2 2 1 - 9

23
1 2 3 4 4 3 3 2 1 - 9

24
1 2 3 4 4 4 3 2 1 - 9

25
1 2 3 4 5 4 3 2 1 - 9

26
1 2 3 4 5 4 3 2 1 1 - 10
"""
