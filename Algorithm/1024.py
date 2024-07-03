# X+1부터 i개 숫자의 합
#   x+1 + x+2 + x+3 + ... + x+i
# = i/2(x+1+x+i)
# = ix+ i/2*(i+1)
# = N

N, L = map(int, input().split())

for i in range(L, 101):
    ix = N - (i * (i+1) // 2)
    if ix % i == 0:
        x = ix // i
        if x + 1 >= 0:              # 음수가 아닌지 확인
            print(*(i for i in range(x+1, x+i+1)))
            break
else:
    print(-1)
