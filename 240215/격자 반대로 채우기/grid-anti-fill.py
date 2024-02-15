n = int(input())
a = [[0] * n for _ in range(n)]
for i in range(n):
    if i % 2 == 0:
        cnt = n * (i + 1) - (n - 1)
    else:
        cnt = n * (i + 1)
    for j in range(n):
        a[j][i] = cnt
        if i % 2 == 0:
            cnt += 1
        else:
            cnt -= 1
a = a[::-1]
for i in range(n):
    a[i] = a[i][::-1]
for i in range(n):
    print(*a[i])