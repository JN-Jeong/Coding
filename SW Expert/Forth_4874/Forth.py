def solve():
    calcs = input().split()
    
    operands = [] # 피연산자
    opers = { # 연산자
        "+" : lambda x, y : x + y,
        "-" : lambda x, y : x - y,
        "*" : lambda x, y : x * y,
        "/" : lambda x, y : x // y
    }

    for calc in calcs:
        if calc == ".":
            if len(operands) > 1: # 숫자만 입력된 경우는 에러
                return "error"
            return operands.pop()
        
        if calc in opers.keys(): # 연산자일 경우
            if len(operands) < 2: # 피연산자가 2개 미만이고 연산자가 나오면 에러
                return "error"
            else:
                num2 = int(operands.pop())
                num1 = int(operands.pop())
                operands.append(opers[calc](num1, num2))
        else: # 피연산자일 경우
            operands.append(calc)

    return operands.pop()



if __name__ == "__main__":
    T = int(input())

    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))