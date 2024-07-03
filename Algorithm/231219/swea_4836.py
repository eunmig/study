T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]
    purple = 0

    for i in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color
                # 두 영역이 겹쳐졌을 때
                if arr[i][j] == 3:
                    purple += 1

    print(f'#{tc} {purple}')