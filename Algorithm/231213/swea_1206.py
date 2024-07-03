T = 10

for tc in range(1, T+1):
    n = int(input())
    building = list(map(int, input().split()))

    result = 0      # 조망권이 확보된 건물의 수

    for i in range(2, n-2):
        height = building[i]

        max_near = max(building[i-2:i] + building[i+1:i+3])     # 주변 건물 중 가장 높은 건물 찾기

        if max_near < height:               # 기준 건물이 최댓값 보다 크다면
            result += height - max_near     # 높이 차를 변수에 저장

    print(f'#{tc} {result}')