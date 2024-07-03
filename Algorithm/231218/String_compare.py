s1 = 'abc'
s2 = 'abc'
s3 = s1[:2] + 'c'
print(s1, s2, s3)       # abc abc abc

if s1 == s3:
    print('s1 == s3')
else:
    print('s1 != s3')
# s1 == s3

if s1 is s3:
    print('s1 is s3')
else:
    print('s1 is not s3')
# s1 is not s3