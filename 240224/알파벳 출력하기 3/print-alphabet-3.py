n = int(input())
c = 65
for i in range(n):
    for j in range(n - i):
        print(chr(c), end = '')
        if chr(c) == 'Z':
            c = 64
        c += 1
    print()