n = int(input())
b = []
for i in range(2, n+1):
    a = []
    for j in range(1, i+1):
        if i % j == 0:
            a.append(j)
    if len(a) == 2:
        b.append(i)
print(*b)