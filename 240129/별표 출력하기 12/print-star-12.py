n = int(input())
print('* ' * n)
for i in range(1, n):
    for j in range(n):
        if j >= i and j % 2 != 0:
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()