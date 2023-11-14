"""
프로그래머스 : 당구 연습
"""


def solution(m, n, startX, startY, balls):
    answer = []

    def distance(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    for endX, endY in balls:
        up, down, left, right = float("inf"), float("inf"), float("inf"), float("inf")
        if not (startX == endX and startY > endY):
            down = distance(startX, -startY, endX, endY)
        if not (startX > endX and startY == endY):
            left = distance(-startX, startY, endX, endY)
        if not (startX == endX and startY < endY):
            up = distance(startX, 2 * n - startY, endX, endY)
        if not (startX < endX and startY == endY):
            right = distance(2 * m - startX, startY, endX, endY)
        answer.append(round((min(up, down, left, right) ** 2)))

    return answer


if __name__ == "__main__":
    ms = [10, 10, 10, 10, 10]
    ns = [10, 10, 10, 10, 10]
    startX = [3, 5, 5, 9, 1]
    startY = [7, 9, 1, 5, 2]
    balls = [[[7, 7], [2, 7], [7, 3]], [[5, 8]], [[5, 2]], [[8, 5]], [[2, 5]]]
    result = [[52, 37, 116], [9], [9], [9], [9]]

    for i, data in enumerate(zip(ms, ns, startX, startY, balls)):
        m, s, sx, sy, b = data
        print(f"#{i}", solution(m, s, sx, sy, b))
