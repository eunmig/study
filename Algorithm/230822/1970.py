import sys
sys.stdin = open('1970.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8

    for i in range(8):
        if N // money[i] > 0:
            # 해당 금액 change 인덱스에 몫 넣기
            change[i] += N // money[i]
            # 거슬러준 금액 제외하고 다시 금액 재세팅
            N = N % money[i]

    print(f'#{tc}')
    print(*change)