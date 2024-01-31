n = int(input())
t = n
for i in range(1, n+1):
    for j in range(1, t+1):
        print('%d * %d = %d'%(i, j, i*j), end = '')
        if j == t:
            print()
        else:
            print(' / ', end = '')
    t -= 1