import sys

# w : 가방무게,  n : 금속 종류
w, n = map(int, input().split())

items = []
for _ in range(n):
    # m : 금속의 무게, p : 무게당 금속 가격
    m, p = map(int, input().split())
    items.append((m, p))
# 금속 가격 기준으로 내림차순 정렬
items.sort(key=lambda x : x[1], reverse=True)

result = 0
for m, p in items:
    # 현재 무게가 가방무게보다 작다면
    if w > m:
        # 현재 물품의 전체 수량에 대한 최대 이익을 'result'에 추가
        result += m * p
        # 배낭 무게에서 현재 물품의 무게 뺴기
        w -= m
    # 남은 배낭의 무게가 현재 물품보다 작거나 같다면
    else:
        # 배낭의 남은 용량에 대한 이익을 더하기
        result += w * p
        break

print(result)