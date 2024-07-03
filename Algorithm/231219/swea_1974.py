T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1

    # 행 순회
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[i][j]] += 1
        for k in range(1, 10):
            if count[k] != 1:
                flag = 0
                break

    # 열순회
    for j in range(9):
        count = [0] * 10
        for i in range(9):
            count[arr[i][j]] += 1
        for k in range(1, 10):
            if count[k] != 1:
                flag = 0
                break

    # 3*3
    for i in range(3):
        for j in range(3):
            count = [0] * 10
            for k in range(3):
                for l in range(3):
                    count[arr[3*i+k][3*j+l]] += 1
            for k in range(1, 10):
                if count[k] != 1:
                    flag = 0
                    break

    print(f'#{tc} {flag}')
