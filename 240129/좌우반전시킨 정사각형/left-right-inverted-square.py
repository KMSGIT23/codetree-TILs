n = int(input())
h = 0
for i in range(n, n**2+1, n):
    h += 1
    for j in range(i, i//n-1, -h):
        print(j, end = ' ')
    print()