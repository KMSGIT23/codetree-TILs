a = input()
b = input()
while b in a:
    for i in range(len(b), len(a)+len(b)):
            if a[i-len(b):i] == b:
                a = list(a)
                del a[i-len(b)]
                del a[i-2]
                a = ''.join(a)
print(a)