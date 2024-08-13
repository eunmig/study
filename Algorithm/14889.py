import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
result = 10e9

def dfs(people, idx):
    global result

    # 팀이 반으로 나눠졌을 때
    if people == n // 2:
        # 각팀 능력치 초기화
        team_start = 0
        team_link = 0

        for i in range(n):
            for j in range(n):
                # 방문하면 start 팀으로 배정
                if visited[i] and visited[j]:
                    team_start += s[i][j]

                # 방문하지 않은 팀 link 팀으로 배정
                elif not visited[i] and not visited[j]:
                    team_link += s[i][j]

        # 경험치 차이가 최소가 되는 경우 찾기
        result = min(result, abs(team_start-team_link))

    # 팀 나누기
    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(people+1, i+1)
                visited[i] = False

dfs(0, 0)
print(result)