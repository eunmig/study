def dfs(point):
    global sum_v, max_v

    # 반복이 끝나면
    if point == n:
        # 최대 점수 갱신
        if sum_v > max_v:
            max_v = sum_v

    for i in range(n):
        if visited[i] == 0:             # 방문하지 않았다면
            visited[i] = 1              # 방문표시
            sum_v += score[point][i]    # 방문한 위치의 점수 합산

            dfs(point+1)                # 다음 행으로 이동

            visited[i] = 0              # 방문표시 초기화 -> 백트레킹
            sum_v -= score[point][i]    # 점수 초기화

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n   # 방문표시할 리스트
    sum_v = 0           # 총 점수를 구할 변수
    max_v = 0           # 최대 점수를 구할 변수

    dfs(0)

    print(f'#{tc} {max_v}')
