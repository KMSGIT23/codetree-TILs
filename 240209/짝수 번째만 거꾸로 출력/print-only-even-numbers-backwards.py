w = input()
a = list(w)
a.reverse()
for i in range(len(w)):
    if i % 2 == 0:
        print(a[i], end = '')