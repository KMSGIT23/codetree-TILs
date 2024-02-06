n, m = map(int, input().split())
a = [
    list(map(int, input().split()))
    for _ in range(m)
]
b = [
    list(map(int, input().split()))
    for _ in range(m)
]
c = [[0]*m for i in range(m)]
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            c[i][j] = 1
for i in range(n):
    print(*c[i])