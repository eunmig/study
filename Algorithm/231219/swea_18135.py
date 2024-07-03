T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    count = 0

    for i in range(1, 1<<n):
        sum_set = 0
        for j in range(n):
            if i & (1<<j):
                sum_set += arr[j]

        if sum_set == 0:
            count += 1
            break

    print(f'#{tc} {count}')
