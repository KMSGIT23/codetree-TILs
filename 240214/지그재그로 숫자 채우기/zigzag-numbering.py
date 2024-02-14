n, m = map(int, input().split())
a = [[0] * n for _ in range(n)]
for i in range(n):
    if i % 2 == 0:
        cnt = n * (i + 1) - (n - 1)
    else:
        cnt = n * (i + 1)
    for j in range(n):
        a[j][i] = cnt - 1
        if i % 2 == 0:
            cnt += 1
        else:
            cnt -= 1
for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()