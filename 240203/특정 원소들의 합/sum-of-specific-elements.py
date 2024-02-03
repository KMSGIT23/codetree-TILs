a = [[0] for _ in range(4)]
c = 0
for i in range(4):
    b = list(map(int, input().split()))
    a[i] = b
for i in range(4):
    for j in range(i+1):
        c += a[i][j]
print(c)