a = input()
b = input()
if b in a:
    for i in range(2, len(a)+2):
        if a[i-2:i] == b:
            print(i-2)
elif b == a:
    print(0)
else:
    print(-1)