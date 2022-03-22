T = int(input())

def binarySearch(start, end, page, count):
    if start > end:
        return 1000
    
    else:
        mid = (start + end) // 2
        print("mid : ", mid)
        # print("pages[mid-1] : ", pages[mid-1])
        # print("page : ", page)
        if page == mid:
            return count
        elif page < mid:
            return binarySearch(start, mid-1, page, count+1)
        else:
            return binarySearch(mid+1, end, page, count+1)

        # 이렇게 쓰면 틀림, 왜지..? mid-1, mid+1이 무슨 차이인 것일까 
        # => 문제 예제를 보면 첫 번째 탐색 : l=1, r=400, c=200, 두 번째 탐색 : l=200, r=400, c=300으로 mid-1, mid+1을 해주지 않음
        # => 문제 그대로 구현해주도록 하자
        # start 값을 0으로 줄 때와 1로 줄 때도 차이가 있다.
        # start 값을 0으로 주고 mid만 쓰면 틀림
        # if page == mid: 
        #     return count
        # elif page < mid:
        #     return binarySearch(start, mid-1, page, count+1)
        # else:
        #     return binarySearch(mid+1, end, page, count+1)


for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    
    a = binarySearch(1, P, Pa, 0)
    b = binarySearch(1, P, Pb, 0)

    print(a, b)
    if a < b:
        print("#{} {}".format(t, "A"))
    elif a > b:
        print("#{} {}".format(t, "B"))
    else:
        print("#{} {}".format(t, 0))
