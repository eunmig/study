T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0

    for i in range(n):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i

    result = abs(max_idx - min_idx)

    print(f'#{tc} {result}')