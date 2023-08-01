"""
8. String to Integer (atoi)
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        answer = ""
        sign = 1
        digit_flag = False  # 숫자 등장 유무
        char_flag = False  # 문자 등장 유무
        for c in s:
            if digit_flag and c.isdigit() == False:
                break
            elif char_flag and c.isdigit() == False:
                break

            if c == " " and digit_flag == False:
                continue
            elif c == "-" and digit_flag == False:
                char_flag = True
                sign = -1
            elif c == "+" and digit_flag == False:
                char_flag = True
                sign = 1
            elif c.isdigit():
                answer += c
                digit_flag = True
            else:
                char_flag = True
                digit_flag = True
                break

        if answer:
            answer = sign * int(answer)
            if answer < -(2**31):
                answer = -(2**31)
            elif answer >= 2**31:
                answer = (2**31) - 1
        else:
            answer = 0
        return answer


if __name__ == "__main__":
    solution = Solution()
    s = ["42", "   -42", "4193 with words", "words and 987", ".1", "+-12"]
    output = [42, -42, 4193, 0, 0, 0]

    for c in s:
        print("#", solution.myAtoi(c))
