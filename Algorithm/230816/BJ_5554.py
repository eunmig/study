import sys
sys.stdin = open('import.txt')

time = [int(input()) for _ in range(4)]

sum_time = 0

for i in time:
    sum_time += i

min, sec = 0, 0
if sum_time % 60 < 60:
    min = sum_time // 60
    sec = sum_time % 60

print(min)
print(sec)