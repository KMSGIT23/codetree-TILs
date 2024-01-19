n = int(input())
a = []
for i in range(n):
    p = int(input())
    a.append(p)
a.sort()
for i in range(n):
    if a[i] % 3 == 0:
        print(a[i])