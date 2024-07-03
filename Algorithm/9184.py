# 0~20 까지는 20으로 항상 값이 같다.
# 값을 저장해 둘 3차원 배열이 필요
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

def DP(a, b, c):
    if (a <=0 or b <= 0 or c <= 0):
        return 1
    if (a > 20 or b > 20 or c > 20):
        return DP(20, 20, 20)

    # 이미 배열에 들어가있으면 출력
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c :
        dp[a][b][c] = DP(a, b, c-1) + DP(a, b-1, c-1) - DP(a, b-1, c)
        return dp[a][b][c]
    else:
        dp[a][b][c] = DP(a-1, b, c) + DP(a-1, b-1, c) + DP(a-1, b, c-1) - DP(a-1, b-1, c-1)
        return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break
    print(f'w({a}, {b}, {c}) = {DP(a, b, c)}')
