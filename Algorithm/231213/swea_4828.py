# 1_bubblesort
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    max_num = arr[n-1]
    min_num = arr[0]
    num_value = max_num - min_num

    print(f'#{tc} {num_value}')

# 2
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    max_num = arr[0]
    min_num = 10e9

    for i in range(1, n):
        if max_num < arr[i]:
            max_num = arr[i]
        if min_num > arr[i]:
            min_num = arr[i]

    num_value = max_num - min_num

    print(f'#{tc} {num_value}')