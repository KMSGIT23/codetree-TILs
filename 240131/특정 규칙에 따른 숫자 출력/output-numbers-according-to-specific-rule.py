n = int(input())
cnt = 0
q = 1
for i in range(n, 0, -1):
    print(' ' * cnt, end = '')
    for j in range(i, 0, -1):
        if q == 10:
            q = 1
        print(q, end = ' ')
        q += 1
    cnt += 2
    print()