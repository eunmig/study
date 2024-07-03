T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    count = 0               # 합이 0이 되는 개수 카운트
    n = len(arr)

    # 0부터 출력하면 공집합 포함
    # 공집합 제외 1부터 출력
    for i in range(1, 1<<n):
        sum_set = 0         # 부분집합 계산
        # n만큼 비트 계산
        for j in range(n):
            # i의 j번째 비트가 1인지 아닌지를 검사하여 부분집합 출력
            if i & (1<<j):
                sum_set += arr[j]

        if sum_set == 0:
            count += 1
            break

    print(f'#{tc} {count}')
