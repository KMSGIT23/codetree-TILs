n = int(input())
a = []
for i in range(n):
    p = int(input())
    a.append(p)
a = sorted(a)
for i in a:
    if i % 3 == 0:
        print(i)