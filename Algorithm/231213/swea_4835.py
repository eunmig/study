T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_num = []

    for i in range(N-(M-1)):
        new_arr = arr[i:i+M]
        curr = 0

        for j in new_arr:
            curr += j
        sum_num.append(curr)

    min_num = 10e9
    max_num = 0

    for i in sum_num:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i

    num_value = max_num - min_num
    print(f'#{tc} {num_value}')