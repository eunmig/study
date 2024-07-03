T = int(input())

for tc in range(1, T+1):
    # k : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # n : 정류장 수
    # m : 충전기가 설치된 m개의 정류장 번호
    k, n, m = map(int, input().split())

    charge_position = list(map(int, input().split()))

    now = 0     # 현재 위치
    cnt = 0     # 충전 횟수

    # 최대 이동거리가 총 정류장 수 보다 작을 때
    while now + k < n:
        # 이동가능 범위에서 뒤로가면서 확인
        for i in range(k, 0, -1):
            # 이동하는 위치가 충전소라면
            if now + i in charge_position:
                now += i        # 이동한만큼 현재거리 갱신
                cnt += 1        # 충전횟수 + 1
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')