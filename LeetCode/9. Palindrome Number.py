"""
9. Palindrome Number
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    x = [121, -121, 10]
    output = [True, False, False]

    for c in x:
        print("#", solution.isPalindrome(c))
