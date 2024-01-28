n = int(input())
a, b = n, 1
for i in range(n*2):
    if i % 2 == 0:
        print('* ' * a)
        a -= 1
    else:
        print('* ' * b)
        b += 1