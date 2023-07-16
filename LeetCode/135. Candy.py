from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        answer = 0

        n = len(ratings)
        if n == 1:
            return 1

        temp = [1] * n
        ids = []
        for i in range(n):
            ids.append([i, ratings[i]])  # index, rating

        ids.sort(key=lambda x: x[1])
        # print(ids)

        for i, r in ids:
            if i == 0:
                if n > 1 and ratings[i] > ratings[i + 1]:
                    temp[i] = temp[i + 1] + 1
            elif i == n - 1:
                if n > 1 and ratings[i] > ratings[i - 1]:
                    temp[i] = temp[i - 1] + 1
            elif 0 < i < n - 1:
                if n > 2 and ratings[i] > ratings[i + 1] and ratings[i] > ratings[i - 1]:
                    temp[i] = max(temp[i - 1], temp[i + 1]) + 1
                elif n > 2 and ratings[i] > ratings[i + 1]:
                    temp[i] = temp[i + 1] + 1
                elif n > 2 and ratings[i] > ratings[i - 1]:
                    temp[i] = temp[i - 1] + 1

        # print(temp)
        answer = sum(temp)

        return answer


if __name__ == "__main__":
    solution = Solution()
    ratings = [[1, 0, 2], [1, 2, 2]]
    output = [5, 4]

    for r in ratings:
        print(solution.candy(r))
