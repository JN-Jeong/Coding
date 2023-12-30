"""
Summer/Winter Coding(~2018)
스티커 모으기(2)
"""


def solution(sticker):
    answer = 0
    N = len(sticker)
    if N == 1:
        return sticker[0]

    # 첫번째 스티커 선택
    dp1 = [0] * N
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, N - 1):
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])

    # 두번째 스티커 선택
    dp2 = [0] * N
    dp2[1] = sticker[1]
    for i in range(2, N):
        dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])

    print("@", dp1, dp2)
    answer = max(dp1[-2], dp2[-1])
    return answer


if __name__ == "__main__":
    stickers = [[14, 6, 5, 11, 3, 9, 2, 10], [1, 3, 2, 5, 4]]
    answer = [36, 8]

    for i, data in enumerate(stickers):
        sticker = data
        print(f"#{i}", solution(sticker))
