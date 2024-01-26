n = int(input())
j = 0
for i in range(n, 0, -1):
    print('*' * i, end = '')
    print(' ' * j, end = '')
    print('*' * i)
    j += 2