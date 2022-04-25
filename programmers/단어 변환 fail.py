"""
(그냥 생각난거 : 편집 거리 알고리즘)
각 단어 문자열이 하나씩 변환되면서 단계를 거쳐야 한다

그래프를 만들어서 푸는 시도 <- 실패
"""

from collections import deque


def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        print("없음")
        return 0
    
    words = [begin] + words
    print(words)
    
    graph = [[0] * (len(words) + 1) for _ in range(len(words) + 1)]
    # print(graph)
    
    for i in range(len(words)-1):
        for j in range(i + 1, len(words)):
            if is_connect(words[i], words[j]):
                graph[i + 1][j + 1] = 1
                graph[j + 1][i + 1] = 1
    
    print(graph)
    
    q = deque()
    q.append((1, 0))
    visited = [0] * (len(words) + 1)
    
    answers = []
    while q:
        idx, count = q.popleft()
        visited[idx] = 1
        
        for i in range(len(graph)):
            if visited[i] == 0 and graph[idx][i] == 1:
                visited[i] = 1
                q.append((i, count + 1))
                print(q)
                
                if i == len(graph) - 1:
                    answers.append(count + 1)
                    
    print(answers)
    answer = min(answers)
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