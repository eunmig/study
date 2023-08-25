T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    # # 내림차순으로 정렬
    # score.sort(reverse=True)
    my_score = 0

    for i in score:
        if score[i] > score[i+1]:
            score[i], score[i+1] = score[i+1], score[i]
    print(score)

    # for i in range(K):
    #     my_score += score[i]
    #
    # print(f'#{tc} {my_score}')

