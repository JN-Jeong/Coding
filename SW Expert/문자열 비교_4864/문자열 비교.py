def solve(): # str2 문자열 내에 str1 문자열이 존재하는지 확인
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    chks = []
    for i in range(N-1 , -1, -1):
        chks.append(str1[i])
    print(chks)

    i = N-1 # str2 인덱스 값
    count = 0
    while i < M:

        j = N-1 # str1 인덱스 값
        while str2[i] == str1[j]: # 문자열들이 일치하는 동안 반복
            if j == 0:
                print(count)
                return 1
            
            i -= 1
            j -= 1

        # if chks.index(str1[j]) > N - j:
        #     i += chks.index(str1[j])
        #     print("idx : ", chks.index(str1[j]))
        # else:
        #     i += N - j
        #     print("idx2 : ", N - j)

        # print("i : ", i)

        # print("i1 : ", i)
        try: 
            i += chks.index(str2[i]) + (N - j - 1)
            print("try i : ", i)
        except:
            i += N + (N - j - 1)
            print("exc i : ", i)

        # print("i2 : ", i)
        count += 1
    
    print(count)
    return 0

def solve1():
    pattern = input()
    text = input()

    skip = list(reversed(pattern))
    matchCnt = 0
    nowIndex = len(pattern) - 1

    # 패턴 매칭 검색
    while matchCnt != len(pattern) and nowIndex < len(text):
        if text[nowIndex] in skip:
            if text[nowIndex] == skip[matchCnt]:
                matchCnt += 1
                nowIndex -= 1
                print(nowIndex)
                continue
            else:
                nowIndex += skip.index(text[nowIndex])
                print(nowIndex)
                matchCnt = 0
        else:
            nowIndex += len(pattern)
            print(nowIndex)
            matchCnt = 0

    if matchCnt == len(pattern):
        return 1
    if nowIndex >= len(text):
        return 0


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        print("#{} {}".format(t, solve()))