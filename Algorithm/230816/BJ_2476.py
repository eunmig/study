import sys
sys.stdin = open('import.txt')

N = int(input())
result = 0
money = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    if a == b == c:  # 3개 동일할 경우
        result = 10000 + a * 1000
    elif a == b or b == c:
        result = 1000 + b * 100
    elif c == a:
        result = 1000 + c * 100
    else:
        result = max(a, b, c) * 100

    if result > money:
        money = result

print(money)

