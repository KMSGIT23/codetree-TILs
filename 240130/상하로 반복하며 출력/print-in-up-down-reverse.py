n = int(input())
for i in range(1, n+1):
    a = []
    a.append(i)
    a.append(n+1-i)
    for j in range(n):
        if j % 2 == 0:
            print(a[0], end = '')
        else:
            print(a[1], end = '')
    print()