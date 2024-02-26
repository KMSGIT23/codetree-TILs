n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            a[i][j] = 1
        if j % 2 == 1:
            a[i][j] = 2
for i in a:
    print(*i)