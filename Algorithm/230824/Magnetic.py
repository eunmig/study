import sys
sys.stdin = open('Magnetic.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1 : N극 -> 바닥에 있는 s극하고 만나려고함, 2 : S극

    # 1-2가 만날때 교착상태 count
    count = 0
    for j in range(N):
        # 열탐색
        # 아래로 내려가면서 탐색
        row, col = 0, j
        # 1-2의 순서인지 stack에 넣었다 뺏다 하며 확인
        stack = []

        while row < N:
            # 스택이 비어있고 1이면 stack에 넣음
            if not stack and arr[row][col] == 1:
                stack.append(1)
            # 스택에 1이 있고 2를 만날경우
            elif stack and arr[row][col] == 2:
                count += stack.pop()
            # 첫번째줄 열탐색이 끝났다면 오른쪽열탐색 시작
            row += 1

    print(f'#{tc} {count}')