"""
2018 KAKAO BLIND RECRUITMENT
[1차] 뉴스 클러스터링

09:00부터 
셔틀 운행 횟수만큼 
셔틀 운행 간격마다
남은 크루가 존재하는지 체크
탑승이 가능한지 체크
탑승 대기 중인 크루가 존재하는지 체크
탑승 할 수 있다면 마지막 셔틀 운행 시간 반환
탑승 할 수 없다면 마지막 탑승한 크루보다 1분 빠른 시간 반환
"""


def solution(n, t, m, timetable):
    answer = ""

    crews = []
    for time in timetable:
        time = time.split(":")
        crews.append(int(time[0]) * 60 + int(time[1]))
    crews.sort()
    busTimes = [540 + i * t for i in range(n)]
    print(crews, busTimes)

    idx = 0  # 다음에 탑승할 크루의 index
    for bt in busTimes:
        r_crew = 0  # 탑승 크루 수
        # 탑승 자리 존재 and 버스 탑승할 크루 존재 and 탑승 대기 크루 존재 하면
        while r_crew < m and idx < len(crews) and crews[idx] <= bt:
            idx += 1
            r_crew += 1

        if r_crew < m:  # 탑승할 자리가 있다면 마지막 버스 운행 시간을 저장
            answer = bt
        else:  # 탑승할 자리가 없다면 마지막으로 탑승한 크루보다 1분 빠른 시간 저장
            answer = crews[idx - 1] - 1

    return min2hour(answer)


def min2hour(time):
    hour = str(time // 60).zfill(2)
    minute = str(time % 60).zfill(2)
    return f"{hour}:{minute}"


n = [1, 2, 2, 1, 1, 10]  # 셔틀 운행 횟수
t = [1, 10, 1, 1, 1, 60]  # 셔틀 운행 간격
m = [5, 2, 2, 5, 1, 45]  # 탑승 가능한 최대 크루 수
timetable = [
    ["08:00", "08:01", "08:02", "08:03"],
    ["09:10", "09:09", "08:00"],
    [
        "09:00",
        "09:00",
        "09:00",
        "09:30",
    ],
    ["00:01", "00:01", "00:01", "00:01", "00:01"],
    ["23:59"],
    [
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
        "23:59",
    ],
]

for (
    n,
    t,
    m,
    time,
) in zip(n, t, m, timetable):
    print(solution(n, t, m, time))
