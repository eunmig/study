import sys
sys.stdin = open('1979.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # 단어가 들어갈 자리
    result = 0

    # 행검사
    for i in range(N):
        count = 0
        for j in range(N):
            # 흰색 부분일때
            if puzzle[i][j] == 1:
                count += 1
                # puzzle의 끝일때
                if j == N-1:
                    if count == K:
                        result += 1
            # 검은색 부분일때
            elif puzzle[i][j] == 0:
                if count == K:
                    result += 1
                count = 0

    # 열검사
    for j in range(N):
        count = 0
        for i in range(N):
            # 흰색 부분일때
            if puzzle[i][j] == 1:
                count += 1
                # puzzle의 끝일때
                if i == N-1:
                    if count == K:
                        result += 1

            # 검은색 부분일떄
            elif puzzle[i][j] == 0:
                if count == K:
                    result += 1
                count = 0

    print(f'#{tc} {result}')