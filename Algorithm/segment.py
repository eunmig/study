
# 세그먼트 디스플레이 정보저장
info = {
    '0' : '1110111',
    '1' : '0010010',
    '2' : '1011101',
    '3' : '1011011',
    '4' : '0111010',
    '5' : '1101011',
    '6' : '1101111',
    '7' : '1110010',
    '8' : '1111111',
    '9' : '1111011',
    ' ' : '0000000'
}

# 테스트 케이스 수
t = int(input())
for _ in range(t):
    a, b = map(str, input().split())

    # 자리수 전처리
    # a, b 길이가 5보다 짧으면 공백을 추가하여 다섯자리로 만들기
    a_zero , b_zero = 5 - len(a), 5 - len(b)
    a = ' ' * a_zero + a
    b = ' ' * b_zero + b

    result = 0

    for i in range(5):
        for j in range(7):
            if info[a[i]][j] != info[b[i]][j]:
                result += 1

    print(result)

