def dfs(x):
    global min_sum, total

    # 탐색이 끝났을 경우
    if x == N:
        if total < min_sum:
            min_sum = total

    # 가지치기
    if total >= min_sum:
        return

    # x != N 경우
    for i in range(N):
        # 방문하지 않았다면
        if visited[i] == 0:
            # 방문표시
            visited[i] = 1
            # 비용 더하기
            total += arr[x][i]

            # 재귀호출
            # 다음 상품 찾아감
            dfs(x+1)

            # 재귀호출이 종료되면 재귀호출 전으로 돌아간다.
            # 방문표시 초기화
            visited[i] = 0
            # 최소비용 초기화
            total -= arr[x][i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # 최소비용 변수
    total = 0
    # 최소비용을 구하기위해 세팅
    min_sum = 10e9

    dfs(0)
    print(f'#{tc} {min_sum}')