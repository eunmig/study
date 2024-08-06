def dfs(queen, row, n):
    count = 0
    # 끝까지 도달했으면 return 1
    if n == row:
        return 1

    for col in range(n):
        # 현재 행에 퀸을 col 열에 배치
        queen[row] = col
        
        for i in range(row):
            # 같은 열에 다른 퀸이 있는 경우
            if queen[i] == queen[row]:
                break
            # 대각선에 다른 퀸이 있는 경우 (기울기-절댓값)
            if abs(queen[i] - queen[row]) == row - i:
                break

        # 다음 행으로 넘어감
        else:
            count += dfs(queen, row + 1, n)

    return count


def solution(n):
    # 퀸의 위치를 저장할 리스트
    return dfs([0] * n, 0, n)

n = 4