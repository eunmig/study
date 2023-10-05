T = int(input())
for tc in range(1, T+1):
    n = int(input())
    p = input()
    k = input()

    # 16진수 -> 10진수 변환
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
           '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13,
           'E': 14, 'F': 15}

    # 다시 16진수로 바꾸는 딕셔너리
    dic_2 = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

    # 암호화 되기전 H를 담을 빈 문자열 생성
    ans = ''
    for i in p:
        val = (dic[i] ^ dic[k])
        # 2자리수 이상이라면 16진수 알파벳으로 변환
        if len(val) == 2:
            val = dic[val]
        ans += val

    print(f'#{tc} {ans}')