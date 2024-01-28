n = int(input())
for i in range(n*2+1):
    if i % 2 == 0:
        print('* ' * (n*2+1))
    else:
        for j in range(1, n+2):
            print('* ', end = '')
            print('  ', end = '')
        print('')