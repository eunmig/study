T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 상하좌우 좌표
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    # 꽃가루의 합을 담을 리스트
    flower = []
    # 최댓값 = 0 세팅
    result = 0


    for i in range(N):
        for j in range(M):
            # 꽃가루 초기값 (좌표에 적힌 꽃가루만큼 퍼져나가서 터짐)
            powder = arr[i][j]
            # 고정 좌표값 (고정 좌표값이 없다면 더해지면서 기준값이 계속 바뀜)
            rose = arr[i][j]
            # 상하좌우 4번 반복
            for k in range(4):
                for l in range(1, rose+1):
                    r1 = i + di[k] * l
                    r2 = j + dj[k] * l
                    if 0 <= r1 < N and 0 <= r2 < M:
                        powder += arr[r1][r2]
            flower.append(powder)

    for i in flower:
        if result < i:
            result = i

    print(f'#{tc} {result}')


