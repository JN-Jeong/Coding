"""
다음 글자가 이전 글자와 다른데 처음 등장한 단어가 아니라면 그룹 단어가 아님

입력받은 단어를 for문으로 한 글자씩 꺼냄
한 글자씩 temp에 저장
처음 등장한 글자라면(이전 글자와 현재 글자가 다르다면) 딕셔너리에 저장
다음 글자가 이전 글자와 다르고 이미 딕셔너리에 저장된 글자라면 False를 반환
for문이 종료될 때까지 False가 반환되지 않았다면 True를 반환

"""

N = int(input())


def check_groupWord(word):
    groupWords = {}
    temp = ""
    for c in word:
        if c != temp:
            if c in groupWords:
                return False
            groupWords[c] = 1
            temp = c
    return True


num = 0
for i in range(N):
    word = input()
    if check_groupWord(word):
        num += 1

print(num)
