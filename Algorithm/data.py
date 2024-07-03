def solution(data, ext, val_ext, sort_by):
    answer = []
    # ext 문자열을 정수로 바꿈
    dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    value = dict[ext]

    for i in data:
        if i[value] < val_ext:
            answer.append(i)

    sort_value = dict[sort_by]

    answer.sort(key=lambda x: x[sort_value])

    return answer