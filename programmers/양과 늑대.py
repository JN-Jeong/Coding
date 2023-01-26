def solution(info, edges):
    answer = []
    visited = [0] * len(info)

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = 1
                if info[child] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[child] = 0
        print(answer)

    visited[0] = 1
    dfs(1, 0)

    return max(answer)


if __name__ == "__main__":
    infos = [[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
    edges = [
        [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]],
        [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]],
    ]
    result = [5, 5]
    for info, edge in zip(infos, edges):
        print(solution(info, edge))
