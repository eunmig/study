n, m = map(int, input().split())

basket = [_ for _ in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())

    new_basket = list(reversed(basket[i-1:j]))
    basket[i-1:j] = new_basket

print(*basket)