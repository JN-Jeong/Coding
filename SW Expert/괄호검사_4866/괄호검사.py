def solve():
    str1 = input()
    brackets = []
    
    for char in str1:
        if char == "{" or char == "(":
            brackets.append(char)
        
        if char == "}":
            if len(brackets) <= 0: # 첫 문자부터 닫는 괄호일 경우
                return 0
            if brackets.pop() != "{":
                return 0
        
        elif char == ")":
            if len(brackets) <= 0: # 첫 문자부터 닫는 괄호일 경우
                return 0
            if brackets.pop() != "(":
                return 0

    if len(brackets) > 0:
        return 0

    return 1

if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))