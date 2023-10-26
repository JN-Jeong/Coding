"""
하나로 연결되어 있는 전력망
전선을 하나 끊어서 하나였던 전력망을 둘로 나눠야 함

전력망이 두 개이기 때문에 송전탑 하나를 시작으로 연결된 송전탑을 모두 방문하여 한 쪽 전력망의 송전탑 개수를 세면 양쪽 전력망의 송전탑 개수를 알 수 있음
연결되어 있는 전선을 하나씩 끊으면서 완전탐색으로 양쪽 송전탑 개수의 차이를 업데이트 해주어서 차이가 가장 적은 값을 반환
"""


uf = []


def find(a):
    global uf
    if uf[a] < 0:
        return a
    uf[a] = find(uf[a])
    return uf[a]


def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return
    uf[pa] += uf[pb]
    uf[pb] = pa


def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n + 1)]
        temp_wire = [wires[x] for x in range(k) if x != i]
        for a, b in temp_wire:
            merge(a, b)
        print("@", uf)
        results = [x for x in uf[1:] if x < 0]
        print("@@", results)
        answer = min(answer, abs(results[0] - results[1]))

    return answer


nums = [9, 4, 7]
wires = [[[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]], [[1, 2], [2, 3], [3, 4]], [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]]
result = [3, 0, 1]

for n, wire in zip(nums, wires):
    print(solution(n, wire))
