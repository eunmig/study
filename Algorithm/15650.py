n, m = map(int, input().split())
ans = []

def dfs():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(1, n+1):
        if i not in ans:
            # 맨 처음 값을 넣을 때 비교 대상이 없기 때문에 분기처리
            if len(ans) == 0:
                ans.append(i)
                dfs()
                ans.pop()

            else:
                # 오름차순
                if i > ans[-1]:
                    ans.append(i)
                    dfs()
                    ans.pop()

dfs()