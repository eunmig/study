s = 'Reverse'
s_lst = list(s)
# print(s_lst)        # ['R', 'e', 'v', 'e', 'r', 's', 'e']

n = len(s)
for i in range(n//2):
    s_lst[i], s_lst[n-1-i] = s_lst[n-1-i], s_lst[i]
# print(s_lst)        # ['e', 's', 'r', 'e', 'v', 'e', 'R']
s = ''.join(s_lst)
# print(s)            # esreveR