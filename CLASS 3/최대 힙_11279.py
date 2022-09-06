# pypy3로 제출
import heapq

N = int(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))

heap: list = []
heapq.heapify(heap)  # 최소 힙 구축
for x in num_list:
    if x == 0:
        if len(heap) > 0:
            print(
                "출력 : ", abs(heapq.heappop(heap))
            )  # 절댓값을 통해 음수로 구성된 원소를 양수로 출력하면 최소값이 최대값으로 출력된다
        else:
            print("출력 : ", 0)
    else:
        heapq.heappush(heap, -x)  # 최소 힙으로 구현된 heapq에 - 를 붙여 음수로 원소를 구성한다
