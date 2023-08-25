import sys
sys.stdin = open('5356.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]

    # arr에서 가장 긴 길이의 단어 찾기
    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    word = ''
    # 열순회로 읽기
    for i in range(max_len):
        for j in range(5):
            try:
                word += arr[j][i]
            except:
                word += ''

    print(f'#{tc} {word}')

# -----------------------------------------------------
# 2
T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]

    # arr에서 가장 긴 길이의 단어 찾기
    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    word = ''
    # 열순회로 읽기
    for i in range(max_len):
        for j in range(5):
            # i행의 길이가 j인덱스보다 길어야 빈공간이 아님
            if i < len(arr[j]):
                # 열순회 리스트에 담기
                word += arr[j][i]

    print(f'#{tc} {word}')
