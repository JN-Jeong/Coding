"""
12. Integer to Roman
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""

        sym_vals = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

        for k, v in sym_vals.items():
            temp = num // v
            num %= v

            answer += k * temp

        return answer


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 58, 1994]
    output = ["III", "LVIII", "MCMXCIV"]

    for n in nums:
        print(solution.intToRoman(n))
