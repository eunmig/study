T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))
    c = [0] * 12

    for i in range(0, len(arr)):
        c[arr[i]] += 1

    i = 0
    tri = run = 0

    while i < 10:
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        i += 1

    if run + tri == 2:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')
