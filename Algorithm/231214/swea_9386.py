T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input()))

    count = 0
    count_num = []

    for i in arr:
        if i == 1:
            count += 1
            count_num.append(count)
        else:
            count = 0

    print(max(count_num))