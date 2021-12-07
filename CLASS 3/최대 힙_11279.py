# 미완료
import heapq

N = int(input())

heap = []
heapq.heapify(heap) # 최소 힙
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) > 0:
            print("출력 : ", abs(heapq.heappop(heap))) # 절댓값을 통해 음수로 구성된 원소를 양수로 출력하면 최소값이 최대값으로 출력된다
        else:
            print("출력 : ", 0)
    else:
        heapq.heappush(heap, -x) # 최소 힙으로 구현된 heapq에 - 를 붙여 음수로 원소를 구성한다