import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

max_val = -10e9
min_val = 10e9

def dfs(idx, total, plus, minus, multiply, divide):
    global max_val, min_val

    if idx == n:
        max_val = max(total, max_val)
        min_val = min(total, min_val)
        return

    if plus:
        dfs(idx + 1, total + num[idx], plus - 1, minus, multiply, divide)
    if minus:
        dfs(idx + 1, total - num[idx], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(idx + 1, total * num[idx], plus, minus, multiply - 1, divide)
    if divide:
        dfs(idx + 1, int(total / num[idx]), plus, minus, multiply, divide - 1)

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_val)
print(min_val)