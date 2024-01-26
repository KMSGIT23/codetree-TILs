n = int(input())
j = n-1
for i in range(1, n*2-1, 2):
    print(' ' * j, end = '')
    print('*' * i)
    j -= 1
j = 0
for i in range(n*2-1, 0, -2):
    print(' ' * j, end = '')
    print('*' * i)
    j += 1