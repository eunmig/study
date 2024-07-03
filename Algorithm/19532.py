# 브루트 포스

a, b, c, d, e, f = map(int, input().split())

# 연립방정식 x,y 구하기
for i in range(-999, 1000):
    for j in range(-999, 1000):
        # 두개의 식이 동시에 만족하는 i, j (=x, y) 찾기
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i, j)
