T = int(input())  # 테스트 케이스 개수
converter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}  # 10 이상의 숫자를 위한 변환기

for tc in range(1, T + 1):
    N, text = input().split()
    result = ''
    for i in text[::-1]:  # 뒤에서부터 탐색
        # 변환기 안에 있다면 변환
        if i in converter:
            i = converter[i]
        i = int(i)  # 변환기 안에 없다면 정수로 변환

        # 16진수는 4자리씩이므로 4번 반복
        for _ in range(4):
            result = str(i % 2) + result
            i //= 2

    print(f'#{tc} {result}')