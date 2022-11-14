"""
1. 벨트와 로봇 한 칸씩 이동
2. 가장 먼저 올라간 로봇부터 벨트가 회전하는 방향으로 한 칸 이동
   이동할 수 없다면 가만히 있음
   이동하려는 칸에 로봇이 없고 그 칸의 내구도가 1이상 남아 있어야 함
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇을 올림
4. 내구도가 0인 칸의 개수가 K개 이상이면 종료, 아니면 1.로 돌아감
"""
from collections import deque


def solution():
    N, K = map(int, input().split())
    belt = deque(list(map(int, input().split())))
    robots = deque([0] * N)
    answer = 0

    while True:
        belt.rotate(1)  # 1단계
        robots.rotate(1)  # 1단계
        print("@ : ", belt)
        print("@@ : ", robots)
        robots[N - 1] = 0  # 로봇 내리는 위치 0

        if sum(robots):  # 로봇이 존재하면
            for i in range(N - 2, -1, -1):  # 가장 먼저 올라간 로봇부터(역순), N-1은 로봇 내리는 위치
                if robots[i] == 1 and robots[i + 1] == 0 and belt[i + 1] >= 1:  # 2단계
                    robots[i + 1] = 1
                    robots[i] = 0
                    belt[i + 1] -= 1  # 내구도 차감
            robots[N - 1] = 0  # 로봇 내리는 위치 0

        if robots[0] == 0 and belt[0] >= 1:  # 3단계
            robots[0] = 1  # 로봇 올림
            belt[0] -= 1  # 내구도 차감
        answer += 1

        if belt.count(0) >= K:  # 4단계
            break

    return answer


if __name__ == "__main__":
    print(solution())
