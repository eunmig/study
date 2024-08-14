import sys
input = sys.stdin.readline

# 행, 열, 대각선 체크 true 반환시 다음 줄 백트레킹
def solution(x):
    for i in range(x):
        # 같은 열에 있거나 대각선이면 false
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x-i:
            return False
    return True

def dfs(x):
    global cnt

    if x == n:
        cnt += 1
    else:
        for i in range(n):
            queen[x] = i
            # true 면 백트래킹
            if solution(x):
                dfs(x+1)

n = int(input())
queen = [0] * n
cnt = 0

dfs(0)
print(cnt)