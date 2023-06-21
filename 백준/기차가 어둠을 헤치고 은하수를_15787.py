def solution():
    N, M = map(int, input().split())
    trains = [0] * (N + 1)
    for _ in range(M):
        command = list(map(int, input().split()))
        if command[0] == 1:
            trains[command[1]] |= 1 << (command[2] - 1)
        elif command[0] == 2:
            trains[command[1]] &= ~(1 << (command[2] - 1))
        elif command[0] == 3:
            trains[command[1]] = trains[command[1]] << 1
            trains[command[1]] &= (1 << 20) - 1
        elif command[0] == 4:
            trains[command[1]] = trains[command[1]] >> 1
        # print(trains)

    trains = set(trains[1:])
    print(len(trains))


if __name__ == "__main__":
    solution()
