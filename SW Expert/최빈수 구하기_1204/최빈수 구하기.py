T = int(input())

for i in range(T):
    case_n = int(input())
    score_list = list(map(int, input().split()))

    score_dict = {}
    for j in range(100, -1, -1):
        score_dict[j] = 0

    for score in score_list:
        score_dict[score] += 1
    
    score_dict = sorted(score_dict.items(), key = lambda item: item[1], reverse=True)
    print("#{} {}".format(case_n, score_dict[0]))