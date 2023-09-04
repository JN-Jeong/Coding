from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        alice = 0
        bob = 0

        turn = 0
        idx = 0
        while idx < len(stoneValue):
            # print(idx, alice, bob)
            if turn % 2 == 0:  # alice turn
                # print("@@@")
                temp = [alice + stoneValue[idx]]
                for i in range(1, 3):
                    if idx + i >= len(stoneValue):
                        continue
                    temp.append(stoneValue[idx + i] + temp[-1])
                # print("@@", temp)

                result = temp[0]
                n_idx = 0
                for i in range(1, len(temp)):
                    if result < temp[i]:
                        result = temp[i]
                        n_idx = i
                alice += result
                idx += n_idx + 1

            else:  # bob turn
                # print("###")
                temp = [bob + stoneValue[idx]]
                for i in range(1, 3):
                    if idx + i >= len(stoneValue):
                        continue
                    temp.append(stoneValue[idx + i] + temp[-1])
                # print("##", temp)

                result = temp[0]
                n_idx = 0
                for i in range(len(temp)):
                    if result < temp[i]:
                        result = temp[i]
                        n_idx = i
                bob += result
                idx += n_idx + 1

            turn += 1
        print(idx, alice, bob)
        if alice > bob:
            return "Alice"
        elif alice < bob:
            return "Bob"
        else:
            return "Tie"
    

if __name__ == "__main__":
    solution = Solution()
    values = [[1, 2, 3, 7], [1, 2, 3, -9], [1, 2, 3, 6], [-2], [-1, -2, -3]]
    output = ["Bob", "Alice", "Tie", "Bob", "Tie"]

    for v in values:
        print(solution.stoneGameIII(v))
