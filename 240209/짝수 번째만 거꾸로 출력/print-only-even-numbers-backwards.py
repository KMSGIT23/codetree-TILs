w = input()
a = list(w)
a.reverse()
if len(w) % 2 == 0:
    for i in range(len(w)):
        if i % 2 == 0:
            print(a[i], end = '')
else:
    b = []
    for i in range(len(w)):
        if i % 2 == 1:
            b.append(a[i])
    b = ''.join(b)
    print(b)