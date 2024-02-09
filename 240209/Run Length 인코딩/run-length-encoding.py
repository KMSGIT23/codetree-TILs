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
a = []
n = 0
for i in b:
    a.append(i[0]+str(len(i)))
a = ''.join(a)
print(len(a))
print(a)