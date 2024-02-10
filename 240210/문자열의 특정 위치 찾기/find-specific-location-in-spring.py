a, b = input().split()
if b in a:
    for i in range(len(a)):
        if a[i] == b:
            print(i)
else:
    print('No')