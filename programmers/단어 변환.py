"""
(그냥 생각난거 : 편집 거리 알고리즘)
각 단어 문자열이 하나씩 변환되면서 단계를 거쳐야 한다

그래프 만들기 없이 해결 시도
"""

from collections import deque


def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        print("없음")
        return 0
    
    q = deque()
    q.append((begin, 0))
    visited = [0] * len(words)
    
    answers = []
    while q:
        word, count = q.popleft()
        if word == target:
            return count
        # visited[0] = 1
        
        for i in range(len(words)):
            if visited[i] == 0 and is_connect(word, words[i]):
                visited[i] = 1
                q.append((words[i], count + 1))
                print(q)
                
    answer = count
    return answer

def is_connect(begin, target):
    count = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            count += 1
    
    if count <= 1:
        return True
    else:
        return False