n, c = map(int, input().split())
if c == 1:
    for i in range(1, n+1):
        print('*' * i)
elif c == 2:
    for i in range(n, 0, -1):
        print('*' * i)
else:
    c = n - 1
    for i in range(1, n*2, 2):
        print(' ' * c, end = '')
        print('*' * i)
        c -= 1