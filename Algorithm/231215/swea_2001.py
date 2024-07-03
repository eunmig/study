T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_sum = 0

    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            kill_bug = 0
            for k in range(m):
                for l in range(m):
                    kill_bug += arr[i+k][j+l]

            if max_sum < kill_bug:
                max_sum = kill_bug

    print(f'#{tc} {max_sum}')