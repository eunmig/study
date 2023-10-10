def dfs(point):
    global sum_v, min_v

    # 마지막에 도달하면
    if point == n:
        if sum_v < min_v:
            min_v = sum_v   # 최대점수 갱신
            return

    for i in range(n):
        if visited[i] == 0:             # 방문하지 않았다면
            visited[i] = 1              # 방문표시하기
            sum_v += score[point][i]    # 총 점수에 해당 위치 점수 더하기

            dfs(point+1)                # 다음 행으로 이동

            visited[i] = 0              # 방문표시 초기화 -> 백트레킹을 위해
            sum_v -= score[point][i]    # 총 점수를 이전으로 되돌리기


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n   # 방문표시 리스트
    sum_v = 0           # 총 점수를 구할 변수
    min_v = 10e9           # 최대 점수를 구할 변수

    dfs(0)

    print(f'#{tc} {min_v}')