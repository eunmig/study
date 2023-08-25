import sys
sys.stdin = open('1974.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    flag = '1'
    for i in range(9):
        # 숫자에 해당하는 인덱스에 1씩 추가
        # 인덱스에 2이상 들어오면 중복된 숫자가 있으니까 0 출력
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            # 가로검사
            row[arr[i][j]] += 1
            if row[arr[i][j]] == 2:
                flag = '0'

            # 세로검사
            col[arr[j][i]] += 1
            if col[arr[j][i]] == 2:
                flag = '0'

    # 3*3 검사
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            r_c = [0] * 10
            for i in range(3):
                for j in range(3):
                    r_c[arr[x+i][y+j]] += 1
                    if r_c[arr[x+i][y+j]] == 2:
                        flag = '0'

    print(f'#{tc} {flag}')
