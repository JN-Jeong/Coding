from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    id_dict = defaultdict(int)
    for i, id in enumerate(id_list):
        id_dict[id] = i
    print(id_dict)

    report_counts = defaultdict(int)
    for r in set(report):
        id1, id2 = r.split()
        report_counts[id2] += 1
    print(report_counts)

    for r in set(report):
        id1, id2 = r.split()
        if report_counts[id2] >= k:
            answer[id_dict[id1]] += 1

    return answer


if __name__ == "__main__":
    id_list = [["muzi", "frodo", "apeach", "neo"], ["con", "ryan"]]
    reports = [["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], ["ryan con", "ryan con", "ryan con", "ryan con"]]
    ks = [2, 3]
    result = [[2, 1, 1, 0], [0, 0]]

    for id, report, k in zip(id_list, reports, ks):
        print(solution(id, report, k))
