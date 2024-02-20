n, k = map(int, input().split())
if k == 1:
    for i in range(1, n+1):
        for j in range(n):
            print(i, end = ' ')
        print()
elif k == 2:
    for i in range(n):
        if i % 2 != 0:
            for j in range(n, 0, -1):
                print(j, end = ' ')
        else:
            for j in range(1, n+1):
                print(j, end = ' ')
        print()
else:
    for i in range(1, n+1):
        for j in range(i, i*n+1, i):
            print(j, end = ' ')
        print()