import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
cnt = 0

for i in range(n):
    s.add(input().rstrip())

for _ in range(m):
    word = input().rstrip()
    print(word)

    if word in s:
        cnt += 1

print(cnt)