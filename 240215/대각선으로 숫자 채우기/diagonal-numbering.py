n, m = map(int, input().split())
a = [[0] * m for i in range(n)]

cnt = 1
for k in range(n+m):
    for i in range(n):
        for j in range(m):
            if k == i + j:
                a[i][j] = cnt
                cnt += 1


for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()