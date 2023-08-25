import sys
sys.stdin = open('import.txt')

a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:
    print('Equilateral')
elif a + b + c == 180:
    if a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')