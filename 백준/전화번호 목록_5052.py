"""
전화번호 목록이 일관성이 있는지 없는지 확인
boolean 반환
Python3는 시간 초과
PyPy3로 제출
"""

def solve():
    tels = []
    for i in range(N):
        tels.append(input())

    tels.sort()
    print(tels)

    for i in range(len(tels)-1):
        if tels[i] == tels[i+1][:len(tels[i])]:
            return "NO"
    
    return "YES"


T = int(input())

for _ in range(T):
    N = int(input())
    print(solve())
    
