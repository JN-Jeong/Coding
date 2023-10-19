"""
프로그래머스 : 과제 진행하기
"""


def solution(plans):
    answer = []
    stack = []

    def time_to_minute(t):
        hour, minute = t.split(":")
        result = int(hour) * 60 + int(minute)

        return result

    for i in range(len(plans)):
        plans[i][1] = time_to_minute(plans[i][1])
        plans[i][2] = int(plans[i][2])

    plans = sorted(plans, key=lambda x: x[1])
    # print(plans)

    for i in range(len(plans) - 1):
        subject1, start_time1, do_time1 = plans[i]
        subject2, start_time2, do_time2 = plans[i + 1]

        end_time = start_time1 + do_time1
        if end_time > start_time2:  # 과제1을 마치지 못함
            stack.append([subject1, 0, end_time - start_time2])  # stack에 과제1 추가

        elif end_time <= start_time2:  # 과제1을 마침
            answer.append(subject1)

            while stack and end_time < start_time2:  # 마치지 못한 과제가 있고 과제2 시작 시간까지 시간이 남으면
                subject3, start_time3, do_time3 = stack.pop()
                end_time = end_time + do_time3
                if end_time > start_time2:
                    stack.append([subject3, 0, end_time - start_time2])
                else:
                    answer.append(subject3)
    answer.append(plans[-1][0])
    for i in range(len(stack) - 1, -1, -1):
        answer.append(stack[i][0])

    return answer


if __name__ == "__main__":
    plans = [
        [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]],
        [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]],
        [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]],
    ]
    result = [["korean", "english", "math"], ["science", "history", "computer", "music"], ["bbb", "ccc", "aaa"]]

    for i, data in enumerate(plans):
        p = data
        print(f"#{i}", solution(p))
