def solve():
    N = int(input())
    players = list(map(int, input().split()))
    # 1 < 2 < 3 < 1 (가위 < 바위 < 보 < 가위)
    return binarySearch(0, N-1, players)+1

def binarySearch(start, end, players):
    if start == end:
        return start

    # 문제에서 주어진 대로 구현 (start, mid / mid+1, end)
    mid = (start+end) // 2
    a = binarySearch(start, mid, players)
    b = binarySearch(mid+1, end, players)
    print("a, b : ", a, b)
    return comp(a, b, players)

def comp(player1, player2, players):
    comp_dict = {
                1 : 2,
                2 : 3,
                3 : 1,
            }

    if comp_dict[players[player1]] == players[player2]: # 카드 값 비교
        return player2
    else:
        return player1


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))