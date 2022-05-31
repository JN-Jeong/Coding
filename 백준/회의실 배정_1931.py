"""
한 회의실에서 겹치지 않게 회의실을 사용할 수 있는 회의의 최대 개수
int 반환
적절한 정렬
"""

N = int(input())

meetings = []
for i in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda item:(item[1], item[0]))   # 회의 종료 시간을 기준으로 오름차순, 회의 종료 시간이 같다면 회의 시작 시간을 기준으로 오름차순 정렬
print(meetings)

end = meetings[0][1] # 가장 먼저 종료되는 회의 시간 저장
meeting = 1

for i in range(1, len(meetings)):
    if end <= meetings[i][0]:               # 회의 종료 시간이 다음 회의 시작 시간보다 작거나 같다면 겹치지 않는 회의 횟수 추가
        print(end)
        end = meetings[i][1]
        meeting += 1

print(end)
print(meeting)