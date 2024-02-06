a = []
b = []
for i in range(3):
    p = list(map(int, input().split()))
    a.append(p)
n = input()
for i in range(3):
    q = list(map(int, input().split()))
    b.append(q)

for i in range(3):
    for j in range(3):
        print(a[i][j] * b[i][j], end = ' ')
    print()