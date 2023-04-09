def solution():
    sound = "quack"
    record = input()

    if len(record) % 5 != 0:
        print(-1)
        return

    answer = 0
    visited = [0] * len(record)
    for i in range(len(record)):
        if record[i] == "q" and visited[i] == 0:
            idx = 0
            first = True
            for j in range(i, len(record)):
                if record[j] == sound[idx] and visited[j] == 0:
                    visited[j] = 1
                    if record[j] == "k":
                        if first:
                            answer += 1
                            first = False
                        idx = 0
                        continue
                    idx += 1
        print(visited)

    if not all(visited) or answer == 0:
        print(-1)
    else:
        print(answer)


if __name__ == "__main__":
    solution()
