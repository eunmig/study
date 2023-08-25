import sys
sys.stdin = open('2805.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 농작물의 가치
    result = 0

    middle = start = end = N // 2

    for i in range(N):
        for j in range(start, end+1):
            result += arr[i][j]
        # middle전까지는 start-end의 간격을 늘린다
        if i < middle:
            start -= 1
            end += 1
        # middle후에 start-end의 간격을 늘린다
        else:
            start += 1
            end -= 1

    print(f'#{tc} {result}')