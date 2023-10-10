T = int(input())
for tc in range(1, T+1):
    n = int(input())
    p = input()
    k = input()

    # 16진수 -> 10진수로 바꾸는 딕셔너리
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
           '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13,
           'E': 14, 'F': 15}

    # 다시 16진수로 바꾸는 딕셔너리
    dic_2 = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

    result = ''
    for i in p:
        val = str(dic[i] ^ dic[k])
        if len(val) == 2:
            val = dic_2[val]
        result += val

    print(f'#{tc} {result}')