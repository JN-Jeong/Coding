def solution():
    N = int(input())
    files = {}
    for _ in range(N):
        file, ext = input().split(".")
        if ext not in files:
            files[ext] = 0
        files[ext] += 1

    for ext in sorted(files):
        print(ext, files[ext])


if __name__ == "__main__":
    solution()
