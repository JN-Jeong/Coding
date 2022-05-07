C = int(input())

for i in range(C):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    above = 0
    for score in scores[1:]:
        if score > avg:
            above += 1

    # print(f"{(above / scores[0]) * 100:.3f}%")
    print("{:.3f}%".format((above / scores[0]) * 100))