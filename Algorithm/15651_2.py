n, m = map(int, input().split())
ans = []

def dfs():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    # 제약 조건 없음
    for i in range(1, n+1):
        ans.append(i)
        dfs()
        ans.pop()

dfs()