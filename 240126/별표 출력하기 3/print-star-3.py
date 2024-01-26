n = int(input())
j = 0
for i in range(n*2-1, 0, -2):
    print(' ' * j, end = '')
    print('* ' * i)
    j += 2