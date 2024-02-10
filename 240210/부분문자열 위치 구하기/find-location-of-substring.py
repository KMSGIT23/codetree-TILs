a = input()
b = input()
if b == a:
    print(0)
elif b in a:
    for i in range(2, len(a)+2):
        if a[i-2:i] == b:
            print(i-2)
else:
    print(-1)