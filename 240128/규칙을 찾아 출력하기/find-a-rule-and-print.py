n = int(input())
j = n - 2
print('* ' * n)
for i in range(1, n):
    print('* ' * i, end = '')
    print('  ' * j, end = '')
    print('*')
    j -= 1