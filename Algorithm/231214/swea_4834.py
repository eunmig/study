T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input()))
    c = [0] * 10        # 0~9 까지 숫자가 적힌 카드 수
    max_num = 0

    for i in range(0, len(arr)):
        c[arr[i]] += 1
        # 가장 많은 장수의 카드 찾기
        max_num = max(max_num, c[arr[i]])


    res_idx = 0
    # 카드 장 수가 같을 때는 적힌 숫자가 큰 쪽을 출력
    for i in range(len(c)-1, -1, -1):
        if c[i] == max_num:
            res_idx = i
            break

    print(f'#{tc} {res_idx} {max_num}')






