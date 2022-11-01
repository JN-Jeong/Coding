"""
수업이 가능한 최소한의 강의실 개수
int 반환
heapq 사용
PyPy3로 제출
"""

import heapq

N = int(input())

lectures = []
for i in range(N):
    lectures.append(list(map(int, input().split())))

# 시작 시간으로 오름차순 정렬, 시작 시간이 같다면 종료 시간을 기준으로 내림차순 정렬
lectures.sort(key=lambda item: (item[0], item[1]))

rooms = []
heapq.heappush(rooms, lectures[0][1])  # 가장 빠른 수업의 종료 시간을 우선순위 큐에 저장

for i in range(1, len(lectures)):  # 첫 수업 이후 수업들 반복
    if rooms[0] > lectures[i][0]:  # 첫 수업 종료 전에 시작되는 수업이라면 강의실 추가
        heapq.heappush(rooms, lectures[i][1])
    else:  # 첫 수업 종료 후에 시작되는 수업이라면 강의실 그대로 사용
        heapq.heappop(rooms)
        heapq.heappush(rooms, lectures[i][1])

print(len(rooms))
