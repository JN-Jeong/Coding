def solution(citations):
    answer = 0
    
    citations = sorted(citations, reverse=True)
    print(citations)
    
    for i, citation in enumerate(citations):
        print(i, citation)
        if i >= citation:
            return i
    answer = len(citations)

    # citations.sort(reverse=True)
    # answer = max(map(min, enumerate(citations, start=1)))

    return answer