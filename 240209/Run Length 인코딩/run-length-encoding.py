a = input()
f = a[0]
n = 0
b = []
for i in range(len(a)):
    if a[i] != f:
        b.append(a[n:i])
        n = i
        f = a[i]
b.append(a[n:])
n = 0
for i in b:
    n += len(i)
print(n)
for i in b:
    print(i[0]+str(len(i)), end = '')