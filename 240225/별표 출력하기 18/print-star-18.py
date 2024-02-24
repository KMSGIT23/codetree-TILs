n = int(input())
cnt = 1
for i in range(n):
    print('  ' * (2 * (n - 1) - (2 * i)), end = '')
    print('* ' * ( 2 * i + 1))