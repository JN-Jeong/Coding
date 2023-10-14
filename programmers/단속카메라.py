"""
프로그래머스 : 단속카메라
"""


def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[1])
    print(routes)

    idx = -30001
    for i in range(len(routes)):
        if idx < routes[i][0]:
            answer += 1
            idx = routes[i][1]

    return answer


if __name__ == "__main__":
    routes = [[[-20, -15], [-14, -5], [-18, -13], [-5, -3]], [[-1, 0], [-1, 0], [-1, 0], [-1, 0]], [[-5, -4], [-4, -3], [-3, -2], [-2, -1], [-1, 0]]]
    result = [2]

    for i, data in enumerate(routes):
        print(f"#{i}", solution(data))
