n, m = map(int, input().split())
a = []
b = []
c = [[0]*m for i in range(n)]
for i in range(n):
    p = list(map(int, input().split()))
    a.append(p)
for i in range(n):
    q = list(map(int, input().split()))
    b.append(q)
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            c[i][j] = 1
for i in range(n):
    print(*c[i])