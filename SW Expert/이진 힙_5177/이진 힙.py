import heapq


def solve():
    N = int(input())

    nodes = list(map(int, input().split()))

    heap = []
    for i in range(len(nodes)):
        heapq.heappush(heap, nodes[i]) # heapq로 이진 최소힙 구성하기
    heap.insert(0, 0) # index가 1부터 시작하도록 하기 위해서 0번째 index 삽입

    sum_ = 0
    idx = len(heap) - 1
    while idx > 0:
        idx = idx // 2
        sum_ += heap[idx]

    return sum_


if __name__ == "__main__":
    T = int(input())

    for i in range(1, T+1):
        print(f"#{i} {solve()}")