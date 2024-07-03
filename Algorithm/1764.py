import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = [input().rstrip() for _ in range(n)]
arr2 = [input().rstrip() for _ in range(m)]

# 교집합 구하기
result = list(set(arr1) & set(arr2))
# 오름차순 정렬
result.sort()

print(len(result))
for i in result:
    print(i)
