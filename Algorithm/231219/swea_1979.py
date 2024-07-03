T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 0

    # 행순회
    for i in range(n):
        count_row = 0
        for j in range(n):
            # 1일때 갯수세기
            if arr[i][j] == 1:
                count_row += 1
            # 0 만났을때 k와 길이가 같은지 확인하고 result += 1
            if arr[i][j] == 0:
                if count_row == k:
                    result += 1
                # count_row 리셋
                count_row = 0
        # 0을 만나지않고 끝났을 경우 k와 길이가 같은지 확인
        if count_row == k:
            result += 1

    # 열순회
    for j in range(n):
        count_low = 0
        for i in range(n):
            # 1일때 갯수세기
            if arr[i][j] == 1:
                count_low += 1
            # 0 만났을때 k와 길이가 같은지 확인하고 result += 1
            if arr[i][j] == 0:
                if count_low == k:
                    result += 1
                # count_low 리셋
                count_low = 0
        # 0을 만나지않고 끝났을 경우 k와 길이가 같은지 확인
        if count_low == k:
            result += 1

    print(f'#{tc} {result}')