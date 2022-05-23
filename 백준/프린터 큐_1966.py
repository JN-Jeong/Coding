if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        q = list(map(int, input().split()))

        count = 0
        i = 0
        while q:
            if max(q) == q[i]:
                count += 1
                if i == M:
                    print(count)
                    break
                q[i] = 0
            
            i += 1
            if i == len(q):
                i = 0


# 패캠 강의 풀이
if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        q = list(map(int, input().split()))
        q = [(i, idx) for idx, i in enumerate(q)]

        count = 0
        while True:
            if q[0][0] == max(q, key=lambda x: x[0])[0]:
                count += 1
                if quit[0][1] == M: # M번째 문서가 맞는지 인덱스 확인
                    print(count)
                    break
                else:
                    q.pop(0)
            else:
                q.append(q.pop(0))