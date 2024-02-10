a = input()
b = input()
if b == a:
    print(0)
elif b in a:
    for i in range(len(b), len(a)+len(b)):
        if a[i-len(b):i] == b:
            print(i-len(b))
            break
else:
    print(-1)