n, m = map(int, input().split())
a = [[0] * n for _ in range(n)]
for i in range(m):
    p, q = map(int, input().split())
    a[p-1][q-1] = 1
for i in range(n):
    print(*a[i])