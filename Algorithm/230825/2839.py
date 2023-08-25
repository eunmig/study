sugar = int(input())

cnt = 0

while sugar >= 0:
    if sugar % 5 == 0:
        cnt = cnt + sugar // 5
        print(cnt)
        break

    sugar -= 3
    cnt += 1

# if구문으로 나누어떨어지지않으면 -1 출력
else:
    print(-1)
