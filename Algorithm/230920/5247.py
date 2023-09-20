from collections import deque

def deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = bfs()

    print(f'#{tc} {result}')