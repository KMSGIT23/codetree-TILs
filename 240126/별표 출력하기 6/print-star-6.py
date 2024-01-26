n = int(input())
j = 0
for i in range(n*2-1, 1, -2):
    print(' ' * j, end = '')
    print('* ' * i)
    j += 2
j = n*2-2
for i in range(1, n*2, 2):
    print(' ' * j, end = '')
    print('* ' * i)
    j -= 2