n = int(input())
t = 65
f = 0
for i in range(n):
    print(' ' * f, end = '')
    for j in range(n, i, -1):
        print(chr(t), end = ' ')
        if t == 90:
            t = 65
        else:
            t += 1
    f += 2
    print()