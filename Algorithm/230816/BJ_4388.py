import sys
sys.stdin = open('import.txt')

socks = [int(input()) for _ in range(5)]
socks_set = set(socks)

for i in socks_set:
    if socks.count(i) % 2 == 1:
        print(i)