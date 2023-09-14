T = 10

for tc in range(1, T+1):
    N = int(input())
    building = list(map(int, input().split()))

    # 조망권이 확보된 건물의 수를 저장할 변수
    result = 0

    # 맨 왼쪽, 오른쪽 두 칸에는 건물이 지어지지않음.
    for i in range(2, N-2):
        height = building[i]
        # 왼쪽, 오른쪽 두칸씩 비교
        max_near = max(building[i-2:i] + building[i+1:i+3])

        # 기준건물이 주변건물의 최대값보다 크다면
        if max_near < height:
            # 기준건물의 높이와 가장 높은 건물의 차를 result에 더하기
            result += height - max_near

    print(f'#{tc} {result}')
