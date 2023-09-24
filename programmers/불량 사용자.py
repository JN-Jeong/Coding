"""
프로그래머스 : 불량 사용자
"""

from itertools import permutations


def solution(user_id, banned_id):
    answer = []

    def check(uid, bid):
        if len(uid) != len(bid):
            return False

        for i in range(len(uid)):
            if bid[i] == "*":
                continue
            if uid[i] != bid[i]:
                return False

        return True

    for uids in permutations(user_id, len(banned_id)):
        cnt = 0
        for uid, bid in zip(uids, banned_id):
            if check(uid, bid):
                cnt += 1
            else:
                break

        if cnt == len(banned_id):
            if set(uids) not in answer:
                answer.append(set(uids))
    print("@", answer)

    return len(answer)


if __name__ == "__main__":
    user_ids = [
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ]
    banned_ids = [["fr*d*", "abc1**"], ["*rodo", "*rodo", "******"], ["fr*d*", "*rodo", "******", "******"]]
    result = [2, 2, 3]

    for i, data in enumerate(zip(user_ids, banned_ids)):
        u, b = data
        print(f"#{i}", solution(u, b))
