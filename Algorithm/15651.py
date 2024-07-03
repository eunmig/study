n, m = map(int, input().split())
ans = []

def back(x):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return

    for i in range(1, n+1):
        # 중복검사 안해야 (1, 1), (2, 2) 같은것도 출력됌
        # if i not in ans:
        ans.append(i)
        back(x+1)       # 오름차순 출력
        ans.pop()

back(1)