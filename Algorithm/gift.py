def solution(friends, gifts):
    # {이름 : {준사람 : 준선물갯수}}
    gifted = {}
    # 선물지수
    gift_idx = {}

    # 딕셔너리 초기화
    for friend in friends:
        gifted[friend] = {}
        gift_idx [friend] = 0

    for gift in gifts:
        # t가 준사람 / f가 받은사람
        t, f = gift.split(' ')
        if f in gifted[t]:
            gifted[t][f] += 1
        else:
            gifted[t][f] = 1

        # 선물 지수 반영
        gift_idx[t] += 1
        gift_idx[f] -= 1

    # 각자 받게 될 선물
    get = [0 for _ in friends]
    for i in range(len(friends)):
        curr = friends[i]  # 인덱스 i에 해당하는 친구
        for j in range(i + 1, len(friends)):
            another = friends[j]  # 인덱스 j에 해당하는 친구
            # curr가 another에게 준 선물 개수
            a = gifted[curr][another] if another in gifted[curr] else 0
            # another가 curr에게 준 선물 개수
            b = gifted[another][curr] if curr in gifted[another] else 0

            if a > b:  # curr가 선물을 더 많이 줬다면
                get[i] += 1
            elif a < b:  # another가 선물을 더 많이 줬다면
                get[j] += 1
            elif a == b:  # 둘이 선물을 주고 받은 개수가 같다면 선물 지수 확인
                ai, bi = gift_idx[curr], gift_idx[another]
                if ai > bi:
                    get[i] += 1
                elif ai < bi:
                    get[j] += 1

    answer = max(get)
    return answer