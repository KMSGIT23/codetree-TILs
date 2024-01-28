n = int(input())
for i in range(n):
    if i % 2 != 0:
        print('* ' * (n - (i - 1) // 2))
    else:
        print('* ' * (1 + (i // 2)))
for i in range(n-1, -1 , -1):
    if i % 2 != 0:
        print('* ' * (n - (i - 1) // 2))
    else:
        print('* ' * (1 + (i // 2)))