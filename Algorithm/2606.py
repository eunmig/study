# DFS
import sys
input = sys.stdin.readline

n = int(input())    # 컴퓨터 개수
v = int(input())    # 연결선 개수

graph = [[] for _ in range(n+1)]    # 그래프 초기화
for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [False] * (n+1)
def dfs(start):
    global cnt
    visited[start] = True   # 시작 지점 방문 처리
    for i in graph[start]:
        if not visited[i]:  # 방문하지 않았으면
            cnt += 1        # 감염된 컴퓨터 +1
            dfs(i)          # 재귀 호출

# 컴퓨터는 1번부터 차례대로 번호가 매겨짐
dfs(1)
print(cnt)