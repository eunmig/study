def find_min(cnt, sum_v):
    global min_v

    #
    if sum(visited) == n:
        sum_v += arr[cnt][0]
        if sum_v < min_v:
            min_v = sum_v
            return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            find_min(i, sum_v + arr[cnt][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    min_v = 1e9
    visited = [0] * n
    visited[0] = 1

    find_min(0, 0)
    print(f'#{tc} {min_v}')