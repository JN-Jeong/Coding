def fiboN(num):
    zero_list = [1, 0]
    one_list = [0, 1]

    if num <= 1:
        return

    for i in range(2, num + 1):  # 0과 1이 출력되는 횟수도 피보나치 수열을 따른다, 결과를 리스트로 만들어둠
        zero_list.append(zero_list[i - 1] + zero_list[i - 2])
        one_list.append(one_list[i - 1] + one_list[i - 2])

    return zero_list, one_list


zero_list, one_list = fiboN(40)

T = int(input())
for _ in range(T):
    num = int(input())
    print(zero_list[num], one_list[num])
