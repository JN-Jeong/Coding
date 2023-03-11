def solution():
    keyboard = ["qwertyuiop", "asdfghjkl0", "zxcvbnm000"]
    locs = {}
    for i in range(len(keyboard)):
        for j in range(len(keyboard[0])):
            locs[keyboard[i][j]] = [i, j]

    # print(locs)
    answer = 0
    left_alpha = "qwertasdfgzxcv"
    right_alpha = "yuiophjklbnm"

    left, right = input().split()
    lloc, rloc = locs[left], locs[right]
    inputs = input()

    for c in inputs:
        if c in left_alpha:
            x1, y1 = lloc
            x2, y2 = locs[c]
            # print(x1, y1, x2, y2)
            # print(abs(x1 - x2) + abs(y1 - y2))
            answer += 1 + abs(x1 - x2) + abs(y1 - y2)
            lloc = [x2, y2]
        elif c in right_alpha:
            x1, y1 = rloc
            x2, y2 = locs[c]
            # print(x1, y1, x2, y2)
            # print(abs(x1 - x2) + abs(y1 - y2))
            answer += 1 + abs(x1 - x2) + abs(y1 - y2)
            rloc = [x2, y2]

    print(answer)


if __name__ == "__main__":
    solution()
