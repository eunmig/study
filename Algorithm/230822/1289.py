import sys
sys.stdin = open('1289.txt')

T = int(input())

for tc in range(1, T+1):
    bit = list(map(int, input()))
    # bit 길이만큼 '0'으로 세팅
    check_bit = [0] * len(bit)
    # 배열을 바꾸는 횟수 count
    count = 0

    # bit 길이만큼 반복
    for i in range(len(bit)):
        # check_ bit와 bit가 같지 않을 경우
        if check_bit[i] != bit[i]:
            # 다른 길이 만큼
            for j in range(i, len(bit)):
                # 바꿔주기
                check_bit[j] = bit[i]
            # 횟수 증가
            count += 1

    print(f'#{tc} {count}')