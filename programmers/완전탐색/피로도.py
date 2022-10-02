from itertools import permutations


def solution(k, dungeons):
    answer = -1

    # ids = list(map(list, permutations(range(len(dungeons)))))
    # for idx in ids:
    for idx in permutations(range(len(dungeons))):
        answer = max(answer, explore(k, idx, dungeons))

    return answer


def explore(k, idx, dungeon):
    cnt = 0
    for i in idx:
        need, use = dungeon[i]
        if k < need:
            continue
        k -= use
        cnt += 1

    return cnt


k = [80]
dungeons = [
    [[80, 20], [50, 40], [30, 10]],
]
results = [3]

for num, dungeon in zip(k, dungeons):
    print(num, dungeon)
    print(solution(num, dungeon))
