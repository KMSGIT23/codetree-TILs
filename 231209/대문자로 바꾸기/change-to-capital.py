a = []

for i in range(5):
    p = list(input().split())
    a.append(p)
for i in range(5):
    for j in range(3):
        a[i][j] = a[i][j].upper()
for i in range(5):
    a[i] = ' '.join(a[i])
    print(a[i])