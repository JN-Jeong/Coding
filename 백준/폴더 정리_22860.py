import sys

sys.setrecursionlimit(10**8)


class Node:
    def __init__(self, name, f_type) -> None:
        self.name = name
        self.type = f_type
        self.folders = []
        self.files = []


def solution():
    N, M = map(int, input().split())
    folders = {}
    for _ in range(N + M):
        parent_folder_name, file_or_folder_name, file_or_folder = input().split()
        if parent_folder_name not in folders:
            folders[parent_folder_name] = Node(parent_folder_name, "1")

        if file_or_folder == "0":  # 1이면 폴더 0이면 파일
            folders[parent_folder_name].files.append(file_or_folder_name)
        else:
            if file_or_folder_name not in folders:
                folders[file_or_folder_name] = Node(file_or_folder_name, "1")
            folders[parent_folder_name].folders.append(folders[file_or_folder_name])

    def search(now):
        files = []
        for n_folder in folders[now].folders:
            print(n_folder.folders, n_folder.files)
            files += search(n_folder.name)
        files += folders[now].files
        return files

    Q = int(input())
    for _ in range(Q):
        path = input().split("/")
        files = search(path[-1])
        print(len(set(files)), len(files))


if __name__ == "__main__":
    solution()
