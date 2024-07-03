T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 달팽이 모양 저장할 2차원 리스트
    snail = [[0] * n for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 초기 위치 및 변수 설정
    # 행, 열, cnt, 방향
    # count = 1 -> 달팽이 1부터 채우기 시작
    i, j, count, dr = 0, 0, 1, 0
    snail[i][j] = count
    # count += 1이 없으면 초기 위치의 값이 0으로 유지되며,
    # 나머지 칸에 대해서는 1부터 시작하여 값이 순차적으로 채워질 것
    count += 1

    # 달팽이 채우기
    while count <= n*n:
        ni, nj = i + di[dr], j + dj[dr]

        # 다음 위치가 범위내에 있고 달팽이가 지나가지않은 경우
        if 0 <= ni < n and 0 <= nj < n and snail[ni][nj] == 0:
            i, j = ni, nj
            snail[i][j] = count
            count += 1
        # 범위를 벗어나거나 달팽이가 다 지나간 경우 방향 변경하여 진행
        # 0 -> 1 -> 2 -> 3 -> 0
        else:
            dr = (dr + 1) % 4

    print(f'#{tc}')
    for lst in snail:
        print(*lst)
