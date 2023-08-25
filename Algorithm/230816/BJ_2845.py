import sys
sys.stdin = open('import.txt')

people, m = map(int, input().split())
human = list(map(int, input().split()))
all = people * m

for i in human:
    print(i - all, end=" ")