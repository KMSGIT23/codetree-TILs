w = input()
a = list(w)
a.reverse()
b = []
for i in range(len(w)):
    if i % 2 == 1:
        b.append(a[i])
print(*b)