a, b = map(int, input().split())
for i in range(1, 10):
    for j in range(b, a-1, -2):
        if j == a:
            print("%d * %d = %d"%(j, i, j*i), end = '')
        else:
            print("%d * %d = %d"%(j, i, j*i), end = ' / ')
    print()