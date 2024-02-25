a = []
b = []
for i in range(9):
    if i < 5:
        if i == 4:
            n = input()
        else:
            p, q = map(int, input().split())
            a.append(p)
            a.append(q)
    else:
        p, q = map(int, input().split())
        b.append(p)
        b.append(q)
for i in range(8):
    print(a[i] * b[i], end = ' ')
    if i % 2 != 0:
        print()