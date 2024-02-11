a = input()
b = input()
while b in a:
    i = a.index(b)
    a = list(a)
    del a[i:i+len(b)]
    a = ''.join(a)
print(a)