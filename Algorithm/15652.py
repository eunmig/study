n, m = map(int, input().split())
ans = []

def dfs():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(1, n+1):
        # 맨 처음 비교 대상 없을 경우
        if len(ans) == 0:
            ans.append(i)
            dfs()
            ans.pop()
        
        else:
            # 비 내림차순
            if i >= ans[-1]:
                ans.append(i)
                dfs()
                ans.pop()

dfs()