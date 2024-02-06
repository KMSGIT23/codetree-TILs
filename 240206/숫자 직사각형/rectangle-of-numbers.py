n, m = map(int, input().split())
a = [[0]*m for _ in range(n)]
q = 1
for i in range(n):
    for j in range(m):
        a[i][j] = q
        q += 1
for i in range(n):
    print(*a[i])