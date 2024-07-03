T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 상하좌우 4방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_sum = 0         # 최대값 초기 세팅

    for i in range(n):
        for j in range(m):
            powder = arr[i][j]      # 기준값
            for k in range(4):
                # 기준점 꽃가루 개수만큼 풍선이 터진다.
                for l in range(1, arr[i][j]+1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < n and 0 <= nj < m:
                        powder += arr[ni][nj]
            if max_sum < powder:
                max_sum = powder

    print(f'#{tc} {max_sum}')