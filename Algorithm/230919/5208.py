def dfs(x):
    global min_change, change

    # 탐색이 끝났을 경우
    if x == N:
        if change < min_change:
            min_change = change

    # 가지치기
    if change >= min_change:
        return

    # 배터리로 갈 수 있는 정류장 탐색
    for i in range(x + 1, x + battery_list[x] + 1):
        # 교체 횟수 +1
        change += 1

        # 재귀호출
        # 다음 버스 정류장 찾아가기
        dfs(i)

        # 재귀호출이 종류되면 교체횟수 초기화
        change -= 1


T = int(input())

for tc in range(1, T+1):
    battery_list = list(map(int, input().split()))
    # 정류장 수
    N = battery_list[0]
    # 배터리 교체 횟수 변수
    change = 0
    # 최소 배터리 교환횟수 비교 변수
    min_change = 10e9

    # battery_list에서 1번부터 배터리 용량
    dfs(1)
    # 최초 배터리 충전횟수 -1
    print(f'#{tc} {min_change-1}')